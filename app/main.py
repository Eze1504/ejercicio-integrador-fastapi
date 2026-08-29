from fastapi import FastAPI

from app.modules.productos.router import router as productos_router


app = FastAPI(
    title="Ejercicio Integrador FastAPI"
)


app.include_router(productos_router)


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}