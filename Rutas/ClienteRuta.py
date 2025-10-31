import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, Depends, HTTPException
from Info.ClienteInfo import ClienteInfo
from Info.ConexionInfoSupabase import getCursor
from Modelos.Modelo import ClienteModel

router = APIRouter(prefix="/Cliente", tags=["Clientes routes"])


clienteInfo = ClienteInfo()


@router.get("/obtener_clientes")
def obtener_clientes(cursor = Depends(getCursor)):
    try:
        res = clienteInfo.obtener_clientes(cursor) 
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/agregar_cliente")
def agregar_cliente(cliente: ClienteModel, cursor = Depends(getCursor)):
    try:
        mensaje = clienteInfo.agregar_cliente(cliente, cursor) 
        return {"mensaje": mensaje}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/modificar_cliente/{id}")
def modificar_cliente(id: int, updatedClient: ClienteModel, cursor = Depends(getCursor)):
    try:
        res = clienteInfo.modifyClient(id, updatedClient, cursor)
        return {"msg": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/eliminar_cliente/{id}")
def eliminar_cliente(id: int, cursor = Depends(getCursor)):
    try:
        res = clienteInfo.deleteClient(id, cursor)
        return {"msg": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
