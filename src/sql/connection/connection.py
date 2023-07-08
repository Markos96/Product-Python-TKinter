from dotenv import load_dotenv
import os
import psycopg2

# Load environment variables from .env files
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

data = {"name_db": DB_NAME, "user_db": DB_USER, "pass_db": DB_PASSWORD, "host_db": DB_HOST, "port_db": DB_PORT}


def get_data():
    return data

