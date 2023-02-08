import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};Server=tcp:primeiro-data-lake.database.windows.net,1433;Database=python-api;Uid=administrador;Pwd=#r00t123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
)

cursor = conn.cursor()