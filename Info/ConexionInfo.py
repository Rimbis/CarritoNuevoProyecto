import os
from typing import Generator
from dotenv import load_dotenv
from psycopg import connect, OperationalError
from psycopg.rows import dict_row  # Para que los resultados sean diccionarios.

# Carga del .env
load_dotenv()

# Variables de conexión
ConnectionString = os.getenv("ConnectionString")
passwordDB = os.getenv("Password")

# Ver si la variable se leyó
print("Intentando conectar con:", ConnectionString)

def get_connection():
    if not ConnectionString:
        raise ValueError("ConnectionString no está configurada")
    try:
        conn = connect(ConnectionString, row_factory=dict_row, sslmode="require")
        return conn
    except OperationalError as e:
        print("Error al conectar a la base de datos:", e)
        raise

def getCursor() -> Generator:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()
