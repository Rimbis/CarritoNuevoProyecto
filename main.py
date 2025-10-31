import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI
from Rutas.ClienteRuta import router as RouterClientes
from Rutas.PedidoRuta import router as RouterPedidos
from Rutas.ProductoRuta import router as RouterProductos



app = FastAPI()
app.include_router(RouterClientes)
app.include_router(RouterProductos)
app.include_router(RouterPedidos)

