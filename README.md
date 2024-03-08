# Taller-1-ing-softw-2
Taller de Desarrollo CRUD

En el presente código, se ha implementado una estructura basada en una arquitectura en capas, haciendo uso de un patrón de diseño Singleton y Strategy. Asimismo, se han adherido a los principios SOLID y de Programación Orientada a Objetos (POO).

# Capa CRUD:
Esta capa constituye el núcleo del archivo y alberga la lógica principal a la que deben adherirse las demás secciones del código.

Detalle de las Funcionalidades en la Capa CRUD:

Se ha implementado el patrón Strategy para gestionar operaciones CRUD de manera flexible. Cada operación (Crear, Leer, Actualizar, Eliminar) se representa como una estrategia concreta que se puede seleccionar dinámicamente.

Clase TareaNotFound:
Esta clase extiende la excepción base y se utiliza para manejar situaciones en las que no se encuentra una tarea específica por su ID.
- class TareaNotFound(Exception):
    def __init__(self, id_tarea):
        self.id_tarea = id_tarea
        super().__init__(f"Tarea con ID {id_tarea} no encontrada.")


Clase OperacionStrategy:
Es una interfaz base que define el método ejecutar, el cual será implementado por las estrategias concretas.

- class OperacionStrategy:
    def ejecutar(self):
        pass

Clases Concretas de Operación (Crear, Leer, Actualizar, Eliminar):
Cada una de estas clases concretas implementa la interfaz OperacionStrategy y proporciona la lógica específica para llevar a cabo la operación correspondiente.

Estas clases se han diseñado para ser utilizadas en conjunto con el patrón Strategy en la Capa CRUD, permitiendo una fácil extensión y modificación de las operaciones CRUD.

Ejemplo con la clase CrearOperacion
class CrearOperacion(OperacionStrategy):
    def __init__(self, crud):
        self.crud = crud

    def ejecutar(self):
        titulo = input("Introduce el título de la tarea: ")
        descripcion = input("Introduce la descripción de la tarea: ")
        self.crud.crear_tarea(titulo, descripcion)

# Capa Notas:
Responsable de la presentación de datos en la terminal y de facilitar el acceso del usuario a las diversas funcionalidades proporcionadas.

En el código, se está aplicando el patrón Strategy de una manera implícita utilizando un diccionario llamado opciones. Cada clave del diccionario representa una opción del menú, y el valor asociado es una referencia a la función que debe ejecutarse cuando se selecciona esa opción. Aquí es donde se evidencia la implementación del patrón Strategy.

En el método main, el bucle se encarga de obtener la opción ingresada por el usuario y luego invoca la función asociada a esa opción utilizando opciones.get(opcion, self.opcion_invalida)(). Esto permite que el comportamiento de cada opción sea independiente y se pueda cambiar fácilmente añadiendo o modificando funciones sin alterar el bucle principal.

Para cada función del diccionario se crea su propia función:
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

# Capa NotasGuardado:
Encargada de gestionar el almacenamiento, modificación y actualización de los datos, desempeñando así el papel de una base de datos.
