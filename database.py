# # Import the required modules for database interaction
# import mysql.connector
# from mysql.connector import Error

# # Define a class for database operations
# class Database:
#     def __init__(self):
#         """
#         Initialize the Database class with a connection to the MySQL database.
#         """
#         try:
#             self.connection = mysql.connector.connect(
#                 host="localhost",         # Replace with your MySQL server host
#                 user="root",     # Replace with your MySQL username
#                 password="", # Replace with your MySQL password
#                 database="supplier_product_db"  # Replace with your MySQL database name
#             )
#             if self.connection.is_connected():
#                 print("Connected to the MySQL database successfully.")
#         except Error as e:
#             print(f"Error while connecting to MySQL: {e}")
#             self.connection = None

#     def fetch_supplier_data(self):
#         """
#         Fetch all supplier data from the 'suppliers' table.
#         """
#         try:
#             cursor = self.connection.cursor(dictionary=True)
#             query = "SELECT * FROM suppliers;"
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Error as e:
#             print(f"Error fetching supplier data: {e}")
#             return []

#     def fetch_product_data(self, filter_query=None):
#         """
#         Fetch product data from the 'products' table, optionally with a filter query.
#         """
#         try:
#             cursor = self.connection.cursor(dictionary=True)
#             query = "SELECT * FROM products"
#             if filter_query:
#                 query += f" WHERE {filter_query}"
#             query += ";"
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Error as e:
#             print(f"Error fetching product data: {e}")
#             return []

#     def execute_custom_query(self, query, params=None):
#         """
#         Execute a custom query with optional parameters.
#         """
#         try:
#             cursor = self.connection.cursor(dictionary=True)
#             cursor.execute(query, params or ())
#             result = cursor.fetchall()
#             return result
#         except Error as e:
#             print(f"Error executing custom query: {e}")
#             return []

#     def close_connection(self):
#         """
#         Close the database connection.
#         """
#         if self.connection and self.connection.is_connected():
#             self.connection.close()
#             print("MySQL database connection closed.")
