import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg
from Modelos.Modelo import ClienteModel

class ClienteInfo:

    def agregar_cliente(self, Cliente: ClienteModel, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO Cliente (Nombre, Apellido) VALUES (%s, %s)",
            (Cliente.Nombre, Cliente.Apellido)
        )
        return "Cliente creado."
        

    def obtener_clientes(self, cursor: psycopg.Cursor) -> list:
        cursor.execute("SELECT id_cliente, Nombre, Apellido FROM Cliente")
        res = cursor.fetchall()
        return [{"id": row[0], "Nombre": row[1], "Apellido": row[2]} for row in res]

    def obtener_cliente_x_id(self, id: int, cursor: psycopg.Cursor) -> list:
        cursor.execute(
            "SELECT id_cliente, Nombre, Apellido FROM Cliente WHERE id_cliente = %s",
            (id,)
        )
        res = cursor.fetchall()
        return [{"id": row[0], "Nombre": row[1], "Apellido": row[2]} for row in res]

    def modifyClient(self, id: int, updatedClient: ClienteModel, cursor: psycopg.Cursor) -> str:
        cursor.execute(
            "UPDATE Cliente SET Nombre = %s, Apellido = %s WHERE id_cliente = %s",
            (updatedClient.Nombre, updatedClient.Apellido, id)
        )
        return "Cliente modificado!"

    def deleteClient(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM Cliente WHERE id_cliente = %s", (id,))
        return "Cliente eliminado"
