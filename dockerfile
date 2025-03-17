FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    gnupg \
    unixodbc-dev

# Add Microsoft repository key and list
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update and install the ODBC Driver for SQL Server
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Upgrade pip and install Python dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your Streamlit app code into the container
COPY . /app

# Expose the default Streamlit port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.enableCORS", "false"]
