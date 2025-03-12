import streamlit as st
import requests

st.title("Database Connection Tester via API")

st.write("Enter your SQL Server connection details and click 'Test Connection'.")

# Input fields for connection details
server = st.text_input("Server", placeholder="your_server_name")
database = st.text_input("Database", placeholder="your_database_name")
uid = st.text_input("Username", placeholder="your_username")
pwd = st.text_input("Password", type="password", placeholder="your_password")

# Button to initiate connection test
if st.button("Test Connection"):
    if not (server and database and uid and pwd):
        st.error("Please fill in all connection details.")
    else:
        # Define your API endpoint URL.
        # For local testing use 'http://localhost:5000/connect'
        # In production, replace with the public URL of your deployed API server.
        API_URL = "http://127.0.0.1:5000/connect"
        
        # Build query parameters to pass to the API server
        params = {
            "server": server,
            "database": database,
            "uid": uid,
            "pwd": pwd
        }
        
        try:
            response = requests.get(API_URL, params=params, timeout=10)
            response.raise_for_status()
            result = response.json()
            if "status" in result:
                st.success(result["status"])
            else:
                st.error("Unexpected response from API.")
        except Exception as e:
            st.error(f"Error: {e}")
