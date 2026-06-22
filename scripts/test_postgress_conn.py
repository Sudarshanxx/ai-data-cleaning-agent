import psycopg2

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "demodb"
DB_USER = "postgres"
DB_PASSWORD = "Suda@123"

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    print("Successfully connected to the PostgreSQL database.")

    # Execute a simple query to test the connection
    cursor.execute("SELECT version();")
    tables =cursor.fetchall()
    print("tables in the database:")
    for table in tables:
        print(table[0])
    
    #close connection
    cursor.close()
    connection.close()
    print("PostgreSQL connection closed.")
except Exception as e:
    print(f"Error connecting to PostgreSQL database: {e}")
   