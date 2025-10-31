import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg
from Modelos.Modelo import ProductoModel


class ProductoInfo:
    def agregar_producto(self, producto: ProductoModel, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO producto (Tipo, Precio) VALUES (%s,%s)",
            (producto.Tipo, producto.Precio),
        )
        return "Producto agregado"

    def obtener_productos(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT * FROM producto").fetchall()
        return [
            {"id_producto": row[0], "Tipo": row[1], "Precio": row[2]} for row in res
        ]