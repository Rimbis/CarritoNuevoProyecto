import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import psycopg
from fastapi import APIRouter, Depends
from Info.ProductoInfo import ProductoInfo
from Info.ConexionInfoSupabase import getCursor
from Modelos.Modelo import ProductoModel

router = APIRouter(prefix="/pedido", tags=["Pedidos routes"])
ProductoInfo = ProductoInfo()

@router.get("/obtener_productos")
def getProductos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = ProductoInfo.obtener_productos(cursor)
    return res


import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))