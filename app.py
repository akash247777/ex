import streamlit as st
import pymssql
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
        conn = pymssql.connect(server=server, user=username, password=password, database=database)
        st.success("Connected successfully!")
        conn.close()
    except Exception as e:
        st.error(f"Connection failed: {e}")

# Button to test the connection
if st.button("Connect"):
    test_connection(server, database, username, password)
