from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import mysql.connector
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Load environment variables securely
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set JWT secret key for signing tokens
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_secret_key')
jwt = JWTManager(app)

# Database connection settings from environment variables
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "supplier_product_db")
}

# Initialize Hugging Face summarization pipeline
summarizer = pipeline("summarization")

# Placeholder for LangGraph - ensure proper installation of langgraph package.
try:
    from langgraph import AgentWorkflow
except ImportError:
    AgentWorkflow = None  # Fallback if LangGraph is unavailable.

# Function to establish DB connection with proper error handling
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise

# Function to retrieve supplier data with SQL injection protection
def fetch_supplier_data(query):
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM suppliers WHERE name LIKE %s", ('%' + query + '%',))
        results = cursor.fetchall()
        cursor.close()
        return results
    except mysql.connector.Error as db_error:
        print(f"Database query error: {db_error}")
        return []
    finally:
        if connection:
            connection.close()

# Function to parse query and summarize response
def process_query(user_query):
    response = {}

    # Use LangGraph workflow if available
    if AgentWorkflow:
        try:
            workflow = AgentWorkflow().parse_query(user_query)
            response = workflow.run()
            if "supplier_data" in response:
                summarized = summarizer(
                    response["supplier_data"],
                    max_length=100,
                    min_length=30,
                    do_sample=False
                )
                response["supplier_summary"] = summarized[0]['summary_text']
        except Exception as e:
            response["error"] = f"Error in LangGraph processing: {str(e)}"
    else:
        # If LangGraph is not available, fallback to DB query
        supplier_data = fetch_supplier_data(user_query)
        response["supplier_data"] = supplier_data
        if supplier_data:
            summarized = summarizer(
                str(supplier_data),
                max_length=100,
                min_length=30,
                do_sample=False
            )
            response["supplier_summary"] = summarized[0]['summary_text']
        else:
            response["error"] = "No supplier data found."

    return response

# Authentication endpoint (Login)
@app.route('/api/login', methods=['POST'])
def login():
    """
    Authenticate user and return a JWT token.
    For simplicity, we are skipping actual authentication logic like checking a database for user credentials.
    Replace with real logic for verifying user credentials.
    """
    user_data = request.json
    username = user_data.get('username')
    password = user_data.get('password')

    # Dummy authentication check (replace this with actual user authentication)
    if username == 'testuser' and password == 'testpassword':
        # Create a JWT token for the user
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Chat endpoint (requires authentication via JWT)
@app.route('/api/chat', methods=['POST'])
@jwt_required()  # Protect this endpoint with JWT authentication
def chat():
    """
    Chat endpoint to handle user queries, process with LangGraph or DB,
    retrieve and summarize data, and return the results. Requires JWT token for access.
    """
    user_query = request.json.get('query')

    if not user_query:
        return jsonify({'error': 'Query parameter is required.'}), 400

    # Retrieve user identity from the JWT token
    current_user = get_jwt_identity()

    try:
        response = process_query(user_query)
        if "error" in response:
            return jsonify({'error': response["error"], 'user': current_user}), 400
        return jsonify({'response': response, 'user': current_user}), 200
    except Exception as e:
        return jsonify({'error': f"Unexpected error: {str(e)}"}), 500

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
