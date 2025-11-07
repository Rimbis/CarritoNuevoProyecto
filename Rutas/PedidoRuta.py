from fastapi import APIRouter, Depends, HTTPException
from Info.PedidoInfo import PedidoInfo
from Info.ConexionInfoSupabase import getCursor
from Modelos.Modelo import PedidoModel
import logging

router = APIRouter(prefix="/pedido", tags=["Pedidos routes"])
pedidoInfo = PedidoInfo()

logging.basicConfig(level=logging.INFO)


@router.post("/crear_pedido")
def crear_pedido(pedido: PedidoModel, cursor = Depends(getCursor)):
    try:
        info = PedidoInfo()
        logging.info(f"Creando pedido: {pedido}")
        res = info.hacer_pedido(pedido, cursor)
        return {"msg": res}
    except Exception as e:
        logging.error(f"Error al crear pedido: {e}")
        raise HTTPException(status_code=500, detail=f"DB error: {e}")


@router.get("/obtener_pedidos")
def obtener_pedidos(cursor = Depends(getCursor)):
    try:
        info = PedidoInfo()
        logging.info("Obteniendo pedidos...")
        res = info.obtener_Pedidos(cursor)
        if not res:
            raise HTTPException(status_code=404, detail="No se encontraron pedidos")
        return res
    except Exception as e:
        logging.error(f"Error al obtener pedidos: {e}")
        raise HTTPException(status_code=500, detail=f"DB error: {e}")
