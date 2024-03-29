class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("hola estoy hablando")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"la habilidad de ser {self.habilidad}"


class PersonalArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(
            f"mi nombre es {self.nombre}, tengo {self.edad} y soy {self.nacionalidad} y tengo {self.mostrar_habilidad()}"
        )


def run():
    artista = PersonalArtista("juan", 20, "peruano", "cantante", 1000, "google")
    artista.presentarse()


if __name__ == "__main__":
    run()
