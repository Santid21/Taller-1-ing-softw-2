from NotasGuardado import NotasGuardadas
class Singleton:
    _instance = None

    def __init__(self):
        if self.__class__._instance is not None:
            raise Exception("No se puede crear una instancia de la clase Singleton")
        self.__class__._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

class CRUD(Singleton):

    def __init__(self):
        super().__init__()
        self.bd = NotasGuardadas()


    def crear_tarea(self, titulo, descripcion):
        self.bd.insertar_tarea(titulo, descripcion)

    def leer_tareas(self):
        return self.bd.obtener_tareas()

    def leer_tarea(self, id_tarea):
        tarea = self.bd.obtener_tarea(id_tarea)
        if tarea:
            return tarea
        else:
            print(f"Tarea con ID {id_tarea} no encontrada.")
            return None

    def actualizar_tarea(self, id_tarea, titulo, descripcion):
        tarea_existente = self.bd.obtener_tarea(id_tarea)
        if tarea_existente:
            self.bd.modificar_tarea(id_tarea, titulo, descripcion)
            print(f"Tarea con ID {id_tarea} actualizada correctamente.")
        else:
            print(f"Tarea con ID {id_tarea} no encontrada. No se pudo actualizar.")

    def eliminar_tarea(self, id_tarea):
        self.bd.borrar_tarea(id_tarea)  