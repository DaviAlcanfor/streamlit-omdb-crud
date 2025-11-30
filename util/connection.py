import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB = os.getenv("DB")
PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("USER")
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

def connect():
    return psycopg2.connect(
        dbname=DB,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )


