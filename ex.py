import streamlit as st
import pyodbc

st.title("Microsoft SQL Server Connection")

server = st.text_input("Server Name")
database = st.text_input("Database Name")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

def test_connection(server, database, username, password):
    try:
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        st.success("Connected successfully!")
        connection.close()
    except Exception as e:
        st.error(f"Connection failed: {e}")

if st.button("Connect"):
    test_connection(server, database, username, password)
