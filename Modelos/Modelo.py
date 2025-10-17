import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# MODELOS
from pydantic import BaseModel


class ClienteModel(BaseModel):
    nombre: str

class ProductoModel(BaseModel):
    tipo: str
    precio: int

class PedidoModel(BaseModel):
    id_cliente: int
    id_producto: int
    cantidad: int