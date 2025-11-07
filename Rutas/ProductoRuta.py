from fastapi import APIRouter, Depends, HTTPException
from Info.ProductoInfo import ProductoInfo
from Modelos.Modelo import ProductoModel
from Info.ConexionInfoSupabase import getCursor
import logging

router = APIRouter(prefix="/producto", tags=["Productos routes"])
productoInfo = ProductoInfo()

logging.basicConfig(level=logging.INFO)

@router.get("/obtener_productos")
def get_productos(cursor = Depends(getCursor)):
    try:
        info = ProductoInfo()
        logging.info("Obteniendo productos...")
        res = info.obtener_productos(cursor)
        if not res:
            raise HTTPException(status_code=404, detail="No se encontraron productos")
        return res
    except Exception as e:
        logging.error(f"Error al obtener productos: {e}")
        raise HTTPException(status_code=500, detail=f"DB error: {e}")

@router.post("/agregar_producto")
def post_producto(producto: ProductoModel, cursor = Depends(getCursor)):
    try:
        info = ProductoInfo()
        logging.info(f"Agregando producto: {producto}")
        res = info.agregar_producto(producto, cursor)
        return {"msg": res}
    except Exception as e:
        logging.error(f"Error al agregar producto: {e}")
        raise HTTPException(status_code=500, detail=f"DB error: {e}")
