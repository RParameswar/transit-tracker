import os
import psycopg2
from dotenv import load_dotenv 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    connection = psycopg2.connect(DATABASE_URL)

    print("Successful connection to the database")

    connection.close()

except Exception as e:

    print(f"Failed connection to the database: {e}")