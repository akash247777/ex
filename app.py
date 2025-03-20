import streamlit as st
import mysql.connector
from mysql.connector import Error

# Streamlit app title
st.title("MySQL Connection Tester")

# Input fields for database credentials
host = st.text_input("Enter Hostname")
user = st.text_input("Enter Username")
password = st.text_input("Enter Password", type="password")
database = st.text_input("Enter Database Name")

# Button to test connection
if st.button("Test Connection"):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Check if connected
        if conn.is_connected():
            st.success("Connected to MySQL database successfully!")
        else:
            st.error("Failed to connect to the MySQL database.")
    
    except Error as e:
        st.error(f"Error: {e}")
    
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
