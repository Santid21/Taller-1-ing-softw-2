# Taller-1-ing-softw-2
Taller de Desarrollo CRUD

En el presente código, se ha implementado una estructura basada en una arquitectura en capas, haciendo uso de un patrón de diseño Singleton y Strategy. Asimismo, se han adherido a los principios SOLID y de Programación Orientada a Objetos (POO).

# Capa CRUD:
Esta capa constituye el núcleo del archivo y alberga la lógica principal a la que deben adherirse las demás secciones del código.

Detalle de las Funcionalidades en la Capa CRUD:

Se ha implementado el patrón Strategy para gestionar operaciones CRUD de manera flexible. Cada operación (Crear, Leer, Actualizar, Eliminar) se representa como una estrategia concreta que se puede seleccionar dinámicamente.

Clase TareaNotFound:
Esta clase extiende la excepción base y se utiliza para manejar situaciones en las que no se encuentra una tarea específica por su ID.
class TareaNotFound(Exception):
    def __init__(self, id_tarea):
        self.id_tarea = id_tarea
        super().__init__(f"Tarea con ID {id_tarea} no encontrada.")


Clase OperacionStrategy:
Es una interfaz base que define el método ejecutar, el cual será implementado por las estrategias concretas.

class OperacionStrategy:
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

# Capa NotasGuardado:
Encargada de gestionar el almacenamiento, modificación y actualización de los datos, desempeñando así el papel de una base de datos.
