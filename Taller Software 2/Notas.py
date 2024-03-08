from CRUD import CRUD

class Notas:

    def __init__(self):
        self.bd = CRUD.get_instance()

    def menu(self):
        print("1. Crear tarea")
        print("2. Ver tareas")
        print("3. Ver una tarea en especifico")
        print("4. Actualizar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        return opcion

    def main(self):
        opciones = {
            "1": self.opcion_crear_tarea,
            "2": self.opcion_ver_tareas,
            "3": self.opcion_ver_tarea_especifica,
            "4": self.opcion_actualizar_tarea,
            "5": self.opcion_eliminar_tarea,
            "6": self.opcion_salir
            
        }

        while True:
            opcion = self.menu()
            opciones.get(opcion, self.opcion_invalida)()

    def opcion_crear_tarea(self):
        titulo = input("Introduce el título de la tarea: ")
        descripcion = input("Introduce la descripción de la tarea: ")
        self.bd.crear_tarea(titulo, descripcion)

    def opcion_ver_tareas(self):
        tareas = self.bd.leer_tareas()
        for tarea in tareas:
            print(tarea)

    def opcion_ver_tarea_especifica(self):
        id_tarea = input("Introduce el ID de la tarea a leer: ")
        tarea = self.bd.leer_tarea(id_tarea)
        print(tarea)

    def opcion_actualizar_tarea(self):
        id_tarea = input("Introduce el ID de la tarea a actualizar: ")
        titulo = input("Introduce el nuevo título de la tarea: ")
        descripcion = input("Introduce la nueva descripción de la tarea: ")
        self.bd.actualizar_tarea(id_tarea, titulo, descripcion)

    def opcion_eliminar_tarea(self):
        id_tarea = input("Introduce el ID de la tarea a eliminar: ")
        self.bd.eliminar_tarea(id_tarea)

    def opcion_salir(self):
        raise StopIteration("Saliendo del programa")

    def opcion_invalida(self):
        print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    notas = Notas()
    notas.main()
