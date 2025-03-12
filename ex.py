import streamlit as st
import pytds

# Streamlit app title
st.title("Microsoft SQL Server Connection")

# Input fields for database credentials
server = st.text_input("Server Name")
database = st.text_input("Database Name")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Function to test the connection
def test_connection(server, database, username, password):
    try:
        connection = pytds.connect(server, database, username, password)
        st.success("Connected successfully!")
        connection.close()
    except Exception as e:
        st.error(f"Connection failed: {e}")

# Button to test the connection
if st.button("Connect"):
    test_connection(server, database, username, password)
