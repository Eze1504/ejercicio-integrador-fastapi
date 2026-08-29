from .schemas import ProductoCreate, ProductoRead, ProductoUpdate

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

def actualizar_producto(
    producto_id: int,
    datos: ProductoUpdate
) -> ProductoRead | None:

    for indice, producto in enumerate(productos):
        if producto.id == producto_id:

            datos_actualizados = producto.model_dump()

            cambios = datos.model_dump(exclude_unset=True)

            datos_actualizados.update(cambios)

            producto_actualizado = ProductoRead(**datos_actualizados)

            productos[indice] = producto_actualizado

            return producto_actualizado

    return None

def alerta_stock(producto_id: int) -> bool | None:
    for producto in productos:
        if producto.id == producto_id:
            return producto.stock < producto.stock_minimo

    return None