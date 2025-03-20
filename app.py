import streamlit as st
import pymssql
import sqlalchemy
# Streamlit app title
st.title("Microsoft SQL Server Connection")

# Input fields for database credentials
server = st.text_input("Server Name",)
database = st.text_input("Database Name",)
username = st.text_input("Username",)
password = st.text_input("Password", type="password")

# Function to test the connection
from sqlalchemy import create_engine

def test_connection(server, database, username, password):
    try:
        connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
        engine = create_engine(connection_string)
        with engine.connect() as conn:
            st.success("Connected successfully!")
    except Exception as e:
        st.error(f"Connection failed: {e}")

# Button to test the connection
if st.button("Connect"):
    test_connection(server, database, username, password)
