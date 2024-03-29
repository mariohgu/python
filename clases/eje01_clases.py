"""
Metodo de resolucion de orden, la manera en que python busca metodos y clases.

"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print(self.nombre, self.edad)


class Estudiate(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_grado(self):
        print(self.grado)


def run():
    estudiate1 = Estudiate("esteban", 20, "bachiller")
    estudiate1.imprimir()
    estudiate1.imprimir_grado()


if __name__ == "__main__":
    run()
