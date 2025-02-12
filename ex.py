import streamlit as st
import pyodbc

# Streamlit app title
st.title("Microsoft SQL Server Connection")

# Input fields for database credentials
server = st.text_input("Server Name",)
database = st.text_input("Database Name",)
username = st.text_input("Username",)
password = st.text_input("Password", type="password")

# Function to test the connection
def test_connection(server, database, username, password):
    try:
        connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        connection = pyodbc.connect(connection_string)
        st.success("Connected successfully!")
        connection.close()
    except Exception as e:
        st.error(f"Connection failed: {e}")

# Button to test the connection
if st.button("Connect"):
    test_connection(server, database, username, password)
