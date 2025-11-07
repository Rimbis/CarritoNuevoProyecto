from fastapi import APIRouter, Depends, HTTPException
from Info.ClienteInfo import ClienteInfo
from Info.ConexionInfoSupabase import getCursor
from Modelos.Modelo import ClienteModel

router = APIRouter(prefix="/cliente", tags=["Clientes routes"])


clienteInfo = ClienteInfo()

@router.get("/obtener_clientes")
def obtener_clientes(cursor = Depends(getCursor)):
    try:
        info = ClienteInfo()
        return info.obtener_clientes(cursor)
    except Exception as e:
        print("Error en obtener_clientes:", e)
        raise HTTPException(status_code=500, detail=f"DB error: {e}")


@router.post("/agregar_cliente")
def agregar_cliente(cliente: ClienteModel, cursor = Depends(getCursor)):
    try:
        info = ClienteInfo()
        mensaje = info.agregar_cliente(cliente, cursor)

        return {"mensaje": mensaje}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/modificar_cliente/{id}")
def modificar_cliente(id: int, updatedClient: ClienteModel, cursor = Depends(getCursor)):
    try:
        info = ClienteInfo()
        res = info.modifyClient(id, updatedClient, cursor)
        return {"msg": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/eliminar_cliente/{id}")
def eliminar_cliente(id: int, cursor = Depends(getCursor)):
    try:
        info = ClienteInfo()
        res = info.deleteClient(id, cursor)
        return {"msg": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
