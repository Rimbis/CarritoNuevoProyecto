import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# MODELOS
from pydantic import BaseModel


class ClienteModel(BaseModel):
    Nombre: str
    Apellido: str

class ProductoModel(BaseModel):
    Tipo: str
    Precio: int

class PedidoModel(BaseModel):
    id_cliente: int
    id_producto: int
    Cantidad: int