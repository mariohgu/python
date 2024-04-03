import math


class Personaje:
    def __init__(self, nombre, habilidad):
        self.nombre = nombre
        self.habilidad = habilidad

    def __add__(self, otro):
        habil = math.pow((self.habilidad + otro.habilidad) / 2, 2)
        return Personaje(self.nombre + otro.nombre, habil)

    def __str__(self):
        return f"Mi nombre es {self.nombre} y mi habilidad es de {self.habilidad}"


p1 = Personaje("Goku", 100)
p2 = Personaje("Vegeta", 100)

p3 = p1 + p2
print(p3)
