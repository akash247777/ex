#!/bin/bash
# Add Microsoft's GPG key
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# Add Microsoft's repository for Ubuntu 20.04
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
# Update package list
apt-get update
# Install the ODBC Driver 17 for SQL Server (accepting the EULA)
ACCEPT_EULA=Y apt-get install -y msodbcsql17
