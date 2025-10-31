import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import psycopg
from fastapi import APIRouter, Depends
from Info.PedidoInfo import PedidoInfo
from Info.ConexionInfoSupabase import getCursor
from Modelos.Modelo import PedidoModel

router = APIRouter(prefix="/pedido", tags=["Pedidos routes"])
PedidoInfo = PedidoInfo()


@router.post("/crear_pedido")
def postPedido(pedido: PedidoModel, cursor: psycopg.Cursor = Depends(getCursor)):
    res = PedidoInfo.addPedido(pedido, cursor)
    return {"msg": res}


@router.get("/obtener_pedidos")
def getPedidos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = PedidoInfo.getPedidos(cursor)
    return res


@router.get("/obtener_pedido/{id}")
def getPedidoForId(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = PedidoInfo.getPedidoForId(id, cursor)
    return res


@router.get("/obtener_pedido_por_cliente/{Nombre}")
def getPedidoForCliente(Nombre: str, Apellido: str, cursor: psycopg.Cursor = Depends(getCursor)):
    res = PedidoInfo.getPedidoForCliente(Nombre, Apellido, cursor)
    return res