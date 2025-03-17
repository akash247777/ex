import streamlit as st
import pyodbc

st.title("SQL Server Connection Test")

# Input fields for credentials
server = st.text_input("Server Name", value="host.docker.internal")  # or your SQL Server IP
database = st.text_input("Database Name", value="your_database")
username = st.text_input("Username", value="your_username")
password = st.text_input("Password", type="password")

def test_connection(server, database, username, password):
    try:
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server},1433;"  # Ensure correct port if needed
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            "Connection Timeout=30;"
        )
        connection = pyodbc.connect(conn_str)
        st.success("Connected successfully!")
        connection.close()
    except Exception as e:
        st.error(f"Connection failed: {e}")

if st.button("Connect"):
    test_connection(server, database, username, password)
