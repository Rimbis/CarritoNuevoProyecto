from Modelos.Modelo import PedidoModel

class PedidoInfo:

    def obtener_Pedidos(self, cursor) -> list:
        try:
            cursor.execute(
                """
                SELECT producto.tipo, producto.precio, cliente.nombre, cliente.apellido
                FROM pedido
                INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente
                INNER JOIN producto ON pedido.id_producto = producto.id_producto
                """
            )
            res = cursor.fetchall()
            return [
                {"producto": row[0], "precio": row[1], "cliente": f"{row[2]} {row[3]}"}
                for row in res
            ]
        except Exception as e:
            raise Exception(f"Error al obtener pedidos: {e}")

    def hacer_pedido(self, pedido: PedidoModel, cursor):
        try:
            cursor.execute(
                "INSERT INTO pedido (id_producto, id_cliente) VALUES (%s, %s)",
                (pedido.id_producto, pedido.id_cliente)
            )
            return "Pedido agregado"
        except Exception as e:
            raise Exception(f"Error al crear pedido: {e}")
