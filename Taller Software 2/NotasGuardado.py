class NotasGuardadas:

    def __init__(self):
        self.tareas = []

    def insertar_tarea(self, titulo, descripcion):
        id_tarea = len(self.tareas) + 1
        self.tareas.append({"id": id_tarea, "titulo": titulo, "descripcion": descripcion})

    def obtener_tareas(self):
        return self.tareas

    def obtener_tarea(self, id_tarea):
        try:
            id_tarea = int(id_tarea)  # Convertir a entero
        except ValueError:
            print("Error: El ID de la tarea debe ser un número entero.")
            return None

        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                return tarea

        print(f"Tarea con ID {id_tarea} no encontrada.")
        return None

    def modificar_tarea(self, id_tarea, titulo, descripcion):
        try:
            id_tarea = int(id_tarea)  # Convertir a entero
        except ValueError:
            print("Error: El ID de la tarea debe ser un número entero.")
            return

        tarea_encontrada = False
        for i in range(len(self.tareas)):
            if self.tareas[i]["id"] == id_tarea:
                self.tareas[i]["titulo"] = titulo
                self.tareas[i]["descripcion"] = descripcion
                print(f"Tarea con ID {id_tarea} modificada correctamente.")
                tarea_encontrada = True
                break

        if not tarea_encontrada:
            print(f"Tarea con ID {id_tarea} no encontrada. No se pudo modificar.")

    def borrar_tarea(self, id_tarea):
        try:
            id_tarea = int(id_tarea)  # Convertir a entero
        except ValueError:
            print("Error: El ID de la tarea debe ser un número entero.")
            return

        tarea_encontrada = False
        for tarea in self.tareas[:]:
            if tarea["id"] == id_tarea:
                self.tareas.remove(tarea)
                print(f"Tarea con ID {id_tarea} eliminada correctamente.")
                tarea_encontrada = True
                break

        if not tarea_encontrada:
            print(f"Tarea con ID {id_tarea} no encontrada. No se pudo eliminar.")
