import os
from typing import Generator
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor


load_dotenv()
passwordDB = os.getenv("Password")  

def get_connection():
    return psycopg2.connect(
        host="db.ifkfcsiowpeyacjplwck.supabase.co",
        database="postgres",
        user="postgres",
        password=passwordDB,
        port=5432,
        cursor_factory=RealDictCursor,
        sslmode="require"
    )

def getCursor() -> Generator[RealDictCursor, None, None]:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()

