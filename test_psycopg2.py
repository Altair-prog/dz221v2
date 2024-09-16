import psycopg2

try:
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_database_user",
        password="your_database_password",
        host="localhost",
        port="5432"
    )
    print("Database connection successful")
except psycopg2.Error as e:
    print(f"Database connection failed: {e}")
finally:
    if conn:
        conn.close()
