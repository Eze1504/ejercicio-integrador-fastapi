from pydantic import BaseModel, Field


class ProductoCreate(BaseModel):
    nombre: str = Field(min_length=1)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)
    stock_minimo: int = Field(ge=0)


class ProductoRead(ProductoCreate):
    id: int


class ProductoUpdate(BaseModel):
    nombre: str | None = None
    precio: float | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    stock_minimo: int | None = Field(default=None, ge=0)