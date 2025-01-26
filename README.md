# AI-Powered Chatbot for Supplier and Product Information

## Project Overview

This project implements an AI-powered chatbot that allows users to query a product and supplier database using natural language. The chatbot is built using the LangGraph framework to handle agent workflows, while an open-source Large Language Model (LLM) such as LLaMA 2 is used for summarizing the information retrieved from a MySQL database.

### Key Features:
- Query a product and supplier database using natural language.
- Use LangGraph for agent workflows.
- Utilize an open-source LLM for summarizing data.
- Frontend is built with React, offering a responsive web interface.
- Backend is built with Python (Flask) and LangGraph.
- MySQL database stores products and suppliers data.
  
## Functional Requirements

- **Product Queries**: "Show me all products under brand X."
- **Supplier Queries**: "Which suppliers provide laptops?"
- **Product Details**: "Give me details of product ABC."
- **LLM Summarization**: The chatbot will enhance responses using context from the LLM.
- **Error Handling**: The system gracefully handles missing or incorrect queries.

## Technical Stack

### Backend:
- **Python (Flask)**: Backend framework for API handling.
- **LangGraph**: Used for managing the chatbot's agent workflows.
- **LLM (LLaMA 2)**: For text summarization and enhancing the data.
- **MySQL**: Database for storing product and supplier data.

### Frontend:
- **React**: For creating a responsive web interface.
- **Material UI**: To style the interface with pre-designed components.
- **Axios**: For API calls to interact with the backend.
- **Redux/Context API**: For state management.

### Database:
- **MySQL**: To store and manage data about suppliers and products.

## Installation:
    ```bash
    git clone https://github.com/your-repository.git
    cd your-repository
    cd backend
    pip install Flask flask-cors transformers mysql-connector-python python-dotenv flask-jwt-extended
    python app.py
    cd frontend
    npm install
    npm run dev