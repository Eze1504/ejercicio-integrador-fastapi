# Ejercicio Integrador FastAPI

Proyecto integrador desarrollado con FastAPI aplicando una estructura modular y separación de responsabilidades.

## Objetivo

Implementar una API REST para la gestión de productos, separando:

- Routers: definición de endpoints y manejo HTTP.
- Schemas: validación y tipado de datos mediante Pydantic.
- Services: lógica de negocio.
- Main: creación de la aplicación y registro de routers.

## Estructura del proyecto

```text
app/
├── __init__.py
├── main.py
└── modules/
    └── productos/
        ├── __init__.py
        ├── router.py
        ├── schemas.py
        └── service.py

tests/
└── productos.http