class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # decorador property para setter y getter
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @edad.deleter
    def edad(self):
        del self.__edad


estudiante = Persona("Carlos", 20)

print(estudiante.nombre)
