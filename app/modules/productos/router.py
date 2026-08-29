from fastapi import APIRouter, HTTPException

from .schemas import ProductoCreate, ProductoRead, ProductoUpdate
from .service import (
    crear_producto,
    listar_productos,
    actualizar_producto,
    alerta_stock
)


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.post("/", response_model=ProductoRead)
def crear(datos: ProductoCreate):
    return crear_producto(datos)


@router.get("/", response_model=list[ProductoRead])
def listar():
    return listar_productos()

@router.put("/{producto_id}", response_model=ProductoRead)
def actualizar(producto_id: int, datos: ProductoUpdate):
    producto = actualizar_producto(producto_id, datos)

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto

@router.get("/{producto_id}/alerta-stock")
def consultar_alerta_stock(producto_id: int):
    alerta = alerta_stock(producto_id)

    if alerta is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {
        "producto_id": producto_id,
        "alerta_stock": alerta
    }