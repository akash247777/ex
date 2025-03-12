import streamlit as st
import pymssql

st.title("Microsoft SQL Server Connection")

server = st.text_input("Server Name (e.g., my-server:1433)")
database = st.text_input("Database Name")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

def test_connection(server, database, username, password):
    try:
        connection = pymssql.connect(
            server=server,
            user=username,
            password=password,
            database=database,
            port=1433,  # Specify the port explicitly
            tds_version='7.0',  # Specify TDS version
            timeout=30  # Add a timeout
        )
        st.success("Connected successfully!")
        connection.close()
    except Exception as e:
        st.error(f"Connection failed: {e}")

if st.button("Connect"):
    test_connection(server, database, username, password)
