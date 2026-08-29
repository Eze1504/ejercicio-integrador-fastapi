from .schemas import ProductoCreate, ProductoRead


productos: list[ProductoRead] = []


def crear_producto(datos: ProductoCreate) -> ProductoRead:
    nuevo_producto = ProductoRead(
        id=len(productos) + 1,
        **datos.model_dump()
    )

    productos.append(nuevo_producto)

    return nuevo_producto


def listar_productos() -> list[ProductoRead]:
    return productos