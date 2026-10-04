from fastapi import APIRouter, HTTPException
from app.database import listar_tareas, crear_tarea, ver_tarea, modificar_tarea, borrar_tarea
from app.modelo_tareas import Tarea, CrearTarea, ActualizarTarea


router = APIRouter(prefix="/tareas", tags=["tareas"])


@router.get("/", response_model=list[Tarea])
def obtener_tareas():
    tareas = listar_tareas()
    return tareas


@router.get("/{id_tarea}", response_model=Tarea)
def obtener_tarea(id_tarea: int):
    tarea = ver_tarea(id_tarea)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@router.post("/", status_code=201, response_model=Tarea)
def crear_nueva_tarea(tarea: CrearTarea):
    tarea_creada = crear_tarea(tarea)
    return tarea_creada


@router.patch("/{id_tarea}", response_model=Tarea)
def actualizar_tarea(id_tarea: int, tarea: ActualizarTarea):
    tarea_actualizada = modificar_tarea(id_tarea, tarea)
    if tarea_actualizada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea_actualizada


@router.delete("/{id_tarea}", status_code=204, response_model=None)
def eliminar_tarea(id_tarea: int):
    tarea_eliminada = borrar_tarea(id_tarea)
    if tarea_eliminada is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return None 