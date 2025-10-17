import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg
from Modelos.Modelo import PedidoModel


class PedidoInfo:
    def obtener_Pedidos(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT Producto.Tipo, producto.Precio, Cliente.Nombre FROM pedido INNER JOIN Cliente ON pedido.id_cliente = Cliente.id_cliente INNER JOIN producto ON pedido.id_producto = producto.id_producto"
        ).fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
        ]



    def hacer_pedido(self, pedido: PedidoModel, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO pedido (id_producto, id_cliente) VALUES (%s,%s)",
            (pedido.id_producto, pedido.id_cliente),
        )
        return "pedido agregado"