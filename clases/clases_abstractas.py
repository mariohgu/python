from abc import ABC, abstractmethod


# Esta clase no se puede usar para crear objetos, ya que sirve como una plantilla. No se puede instanciar
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    # definiendo el metodo como abstracto estamos obligando a implementarlo en las clases hijas
    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(
            f"mi nombre es {self.nombre}, tengo {self.edad} y soy {self.sexo} y me gusta {self.actividad}"
        )


class Estudiante(Persona):
    def __init__(
        self,
        nombre,
        edad,
        sexo,
        actividad,
    ):
        Persona.__init__(self, nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")


estudiante = Estudiante("Carlos", 20, "masculino", "programacion")
estudiante.presentarse()
estudiante.hacer_actividad()

estudiante2 = Estudiante("Jose", 40, "masculino", "arte")
estudiante.presentarse()
estudiante2.presentarse()
