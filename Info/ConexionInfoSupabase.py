import os
from psycopg import connect
from fastapi import HTTPException
from dotenv import load_dotenv

# Carga las variables del .env desde la raíz del proyecto
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

ConnectionString = os.getenv("ConnectionString")

if not ConnectionString:
    raise ValueError("❌ ConnectionString no está configurada en el archivo .env")

def get_connection():
    try:
        conn = connect(ConnectionString, sslmode="require")
        return conn
    except Exception as e:
        print("❌ Error al conectar a la base de datos:", e)
        raise HTTPException(status_code=500, detail=f"DB error: {e}")

def getCursor():
    """Dependency para FastAPI: abre conexión y cursor, y los cierra automáticamente."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        print("❌ Error en getCursor:", e)
        raise HTTPException(status_code=500, detail=f"DB error: {e}")
    finally:
        cursor.close()
        conn.close()
