import streamlit as st
import pyodbc
import os
import platform
import pymssql

# Streamlit app title
st.title("Microsoft SQL Server Connection")

# Configuration section with tabs
tab1, tab2 = st.tabs(["Connection", "About"])

with tab1:
    # Input fields for database credentials
    server = st.text_input("Server Name", value=os.environ.get("DB_SERVER", ""))
    database = st.text_input("Database Name", value=os.environ.get("DB_NAME", ""))
    username = st.text_input("Username", value=os.environ.get("DB_USER", ""))
    password = st.text_input("Password", type="password", value=os.environ.get("DB_PASSWORD", ""))

    # Connection method selection
    connection_method = st.radio(
        "Connection Method",
        ["ODBC Driver (try first)", "pymssql (alternative)"]
    )

    # Function to test connection with ODBC
    def test_odbc_connection(server, database, username, password):
        try:
            # Try different ODBC drivers based on availability
            drivers = [
                "{ODBC Driver 18 for SQL Server}",
                "{ODBC Driver 17 for SQL Server}",
                "{SQL Server Native Client 11.0}",
                "{FreeTDS}"
            ]
            
            connected = False
            error_messages = []
            
            for driver in drivers:
                try:
                    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
                    connection = pyodbc.connect(connection_string)
                    st.success(f"Connected successfully using {driver}!")
                    st.session_state.connection_info = f"Connected using {driver}"
                    connection.close()
                    connected = True
                    break
                except Exception as e:
                    error_messages.append(f"Failed with {driver}: {str(e)}")
                    continue
            
            if not connected:
                st.error("All ODBC connection methods failed:")
                for msg in error_messages:
                    st.error(msg)
                return False
            return True
        except Exception as e:
            st.error(f"Connection error: {e}")
            return False

    # Function to test connection with pymssql
    def test_pymssql_connection(server, database, username, password):
        try:
            conn = pymssql.connect(server=server, user=username, password=password, database=database)
            st.success("Connected successfully using pymssql!")
            st.session_state.connection_info = "Connected using pymssql"
            conn.close()
            return True
        except Exception as e:
            st.error(f"pymssql connection failed: {e}")
            return False

    # Button to test the connection
    if st.button("Connect"):
        if not server or not database or not username or not password:
            st.error("Please fill in all fields")
        else:
            if connection_method == "ODBC Driver (try first)":
                if not test_odbc_connection(server, database, username, password):
                    st.info("Trying alternative connection method (pymssql)...")
                    test_pymssql_connection(server, database, username, password)
            else:
                test_pymssql_connection(server, database, username, password)

    # Environment information
    st.subheader("Environment Information")
    st.write(f"Platform: {platform.system()} {platform.release()}")
    st.write(f"Python Version: {platform.python_version()}")
    
    # Display available ODBC drivers
    try:
        drivers = pyodbc.drivers()
        if drivers:
            st.write("Available ODBC Drivers:")
            for driver in drivers:
                st.write(f"- {driver}")
        else:
            st.write("No ODBC drivers found.")
    except Exception as e:
        st.write(f"Error retrieving ODBC drivers: {e}")

with tab2:
    st.subheader("About This App")
    st.write("""
    This application attempts to connect to a Microsoft SQL Server database using two different methods:
    
    1. ODBC Driver - Tries multiple drivers in sequence
    2. pymssql - A pure Python SQL Server client
    
    For Streamlit Cloud deployment, you can set the following secrets in your GitHub repository:
    - DB_SERVER
    - DB_NAME
    - DB_USER
    - DB_PASSWORD
    
    See Streamlit documentation for more information on setting secrets.
    """)
