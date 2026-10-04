from datetime import datetime
from pydantic import BaseModel


class CrearTarea(BaseModel):
    nombre_tarea: str
    fecha_entrega: datetime | None = None
    terminada: bool = False


class ActualizarTarea(BaseModel):
    nombre_tarea: str | None = None
    fecha_entrega: datetime | None = None
    terminada: bool | None = None


class Tarea(BaseModel):
    id: int
    nombre_tarea: str
    fecha_entrega: datetime | None = None
    terminada: bool = False

