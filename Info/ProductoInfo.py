from Modelos.Modelo import ProductoModel

class ProductoInfo:

    def agregar_producto(self, producto: ProductoModel, cursor):
        try:
            cursor.execute(
                "INSERT INTO producto (tipo, precio) VALUES (%s, %s)",
                (producto.Tipo, producto.Precio),
            )
            return "Producto agregado"
        except Exception as e:
            raise Exception(f"Error al agregar producto: {e}")

    def obtener_productos(self, cursor) -> list:
        try:
            cursor.execute("SELECT * FROM producto")
            res = cursor.fetchall()
            return [
                {"id_producto": row[0], "tipo": row[1], "precio": row[2]}
                for row in res
            ]
        except Exception as e:
            raise Exception(f"Error al obtener productos: {e}")
