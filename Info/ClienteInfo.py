import psycopg
from Modelos.Modelo import ClienteModel

class ClienteInfo:

    def agregar_cliente(self, cliente: ClienteModel, cursor: psycopg.Cursor):
        try:
            cursor.execute(
                "INSERT INTO cliente (nombre, apellido) VALUES (%s, %s)",
                (cliente.Nombre, cliente.Apellido)
            )
            return "Cliente creado."
        except Exception as e:
            raise Exception(f"Error al agregar cliente: {e}")
        


    def obtener_clientes(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM cliente")
        res = cursor.fetchall()
        return [
            {"id_cliente": row[0], "nombre": row[1], "apellido": row[2]}
            for row in res
        ]

    def obtener_cliente_x_id(self, id_cliente: int, cursor: psycopg.Cursor):
        try:
            cursor.execute(
                "SELECT id_cliente, nombre, apellido FROM cliente WHERE id_cliente = %s",
                (id,)
            )
            res = cursor.fetchall()
            return [{"id_cliente": row[0], "nombre": row[1], "apellido": row[2]} for row in res]
        except Exception as e:
            raise Exception(f"Error al obtener cliente por ID: {e}")

    def modifyClient(self, id_cliente: int, updatedClient: ClienteModel, cursor) -> str:
        try:
            cursor.execute(
                "UPDATE cliente SET nombre = %s, apellido = %s WHERE id_cliente = %s",
                (updatedClient.Nombre, updatedClient.Apellido, id_cliente)
            )
            return "Cliente modificado!"
        except Exception as e:
            raise Exception(f"Error al modificar cliente: {e}")

    def deleteClient(self, id_cliente: int, cursor) -> str:
        try:
            cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
            return "Cliente eliminado"
        except Exception as e:
            raise Exception(f"Error al eliminar cliente: {e}")
