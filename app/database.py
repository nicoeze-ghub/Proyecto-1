from app.modelo_tareas import CrearTarea, ActualizarTarea, Tarea

diccionario_tareas = {}
siguiente_id = 1


def listar_tareas():
    return list(diccionario_tareas.values())


def crear_tarea(tarea: CrearTarea):
    global siguiente_id
    id_tarea = siguiente_id
    siguiente_id += 1
    nueva_tarea = Tarea(
        id=id_tarea,
        nombre_tarea=tarea.nombre_tarea,
        fecha_entrega=tarea.fecha_entrega,
        terminada=tarea.terminada
    )
    diccionario_tareas[id_tarea] = nueva_tarea
    return nueva_tarea


def ver_tarea(id_tarea: int):
    return diccionario_tareas.get(id_tarea)


def modificar_tarea(id_tarea: int, tarea: ActualizarTarea):
    tarea_existente = diccionario_tareas.get(id_tarea)
    if tarea_existente:
        if tarea.nombre_tarea is not None:
            tarea_existente.nombre_tarea = tarea.nombre_tarea
        if tarea.fecha_entrega is not None:
            tarea_existente.fecha_entrega = tarea.fecha_entrega
        if tarea.terminada is not None:
            tarea_existente.terminada = tarea.terminada
        return tarea_existente
    return None


def borrar_tarea(id_tarea: int):
    return diccionario_tareas.pop(id_tarea, None)