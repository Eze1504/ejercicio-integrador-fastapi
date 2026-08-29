from fastapi import APIRouter

from .schemas import ProductoCreate, ProductoRead
from .service import crear_producto, listar_productos


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
