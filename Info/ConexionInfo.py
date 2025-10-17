import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sqlite3
from typing import Generator

def getCursor() -> Generator[sqlite3.Cursor, None, None]:
    conn = sqlite3.connect("comercio.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def initeDB() -> None:
        connection = sqlite3.connect("mercado.db", check_same_thread=False)
        try:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS Cliente (id_cliente INTEGER PRIMARY KEY, Nombre TEXT)"
            )
            connection.execute(
                "CREATE TABLE IF NOT EXISTS Producto (id_producto INTEGER PRIMARY KEY, Tipo TEXT, Precio INTEGER, cantidad INTEGER)"
            )
            connection.execute(
                "CREATE TABLE IF NOT EXISTS Pedido (id_pedido INTEGER PRIMARY KEY, id_producto INTEGER, id_cliente INTEGER, FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente), FOREIGN KEY (id_producto) REFERENCES producto(id_producto) )"
            )
            connection.commit()
        finally:
            connection.close()
            print("DB Inicializada")