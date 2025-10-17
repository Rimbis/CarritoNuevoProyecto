import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import psycopg
from fastapi import APIRouter, Depends
from Info.ClienteInfo import ClienteInfo
from Info.ConexionInfoSupabase import getCursor
from Info.ProductoInfo import ProductoInfo
from Modelos.Modelo import ClienteModel

router = APIRouter(prefix="/cliente", tags=["Clientes routes"])
ClienteInfo = ClienteInfo()

class ClienteInfo:
    @router.get("/obtener_clientes")
    def obtener_clientes(cursor: psycopg.Cursor = Depends(getCursor)):
        res = ClienteInfo.obtener_clientes(cursor)
        return res
    
    
    @router.post("/agregar_cliente")
    def agregar_Cliente(cliente: ClienteModel, cursor: psycopg.Cursor = Depends(getCursor)):
        res = ClienteInfo.agregar_Cliente(Cliente, cursor)
        return {"msg": res}

    @router.put("/modificar_cliente/{id}")
    def putCliente(
    id: int, clienteUpdated: ClienteModel, cursor: psycopg.Cursor = Depends(getCursor)
):
        res = clientManager.modifyClient(id, clienteUpdated, cursor)
        return {"msg", res}


    @router.delete("/eliminar_cliente/{id}")
    def deleteCliente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
        res = clientManager.deleteClient(id, cursor)
        return {"msg": res}







