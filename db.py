from flask.json import load
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT"),
        sslmode = os.getenv("DB_SSLMODE")
    )
    cur = conn.cursor()
    print("Conected to db")
    
except Exception as error:
    print(error)


def get_cursor(cursor_factory=None):
    if cursor_factory:
        return conn.cursor(cursor_factory=cursor_factory)
    return conn.cursor()
