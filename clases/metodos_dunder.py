# Funciones que tienen un nombre especial reservado.
# __init__: Se ejecuta cuando se crea un objeto de la clase
# __del__: Se ejecuta cuando se elimina un objeto de la clase
# __str__: Se ejecuta cuando se llama a str() sobre un objeto
# __repr__: Se ejecuta cuando se llama a repr() sobre un objeto
# __len__: Se ejecuta cuando se llama a len() sobre un objeto
# __getitem__: Se ejecuta cuando se accede a un elemento de un objeto
# __setitem__: Se ejecuta cuando se asigna un valor a un elemento de un objeto
# __contains__: Se ejecuta cuando se usa el operador in sobre un objeto
# __iter__: Se ejecuta cuando se itera sobre un objeto
# __next__: Se ejecuta cuando se usa el operador next sobre un objeto
# __add__: Se ejecuta cuando se suma dos objetos
# __sub__: Se ejecuta cuando se resta dos objetos
# __mul__: Se ejecuta cuando se multiplica dos objetos
# __truediv__: Se ejecuta cuando se divide dos objetos
# __floordiv__: Se ejecuta cuando se divide dos objetos y se redondea hacia abajo
# __mod__: Se ejecuta cuando se calcula el residuo de la división de dos objetos
# __pow__: Se ejecuta cuando se eleva un objeto a una potencia
# __lshift__: Se ejecuta cuando se desplaza bits a la izquierda
# __rshift__: Se ejecuta cuando se desplaza bits a la derecha
# __and__: Se ejecuta cuando se realiza una operación AND bit a bit

from abc import ABC, abstractclassmethod


class Animales:

    def __init__(self, especie, familia, color):
        self.especie = especie
        self.familia = familia
        self.color = color

    def velocidad(self, velocidad):
        pass


class Gato(Animales):
    def __init__(self, especie, familia, color):
        super().__init__(especie, familia, color)

    def velocidad(self, velocidad):
        self.velocidad = velocidad
        return self.velocidad * 3


class Perro(Animales):
    def __init__(self, especie, familia, color):
        super().__init__(especie, familia, color)

    def velocidad(self, velocidad):
        self.velocidad = velocidad
        return self.velocidad * 2

    def __str__(self):
        return f"{self.especie} {self.familia} {self.color}"

    def __add__(self, other):
        return Perro(
            self.especie + other.especie,
            self.familia + other.familia,
            self.color + other.color,
        )


perro = Perro("Canilla", "Candonga", "Blanco")
print(perro.velocidad(10))


perro2 = Perro("Canis familiaris", "Canidae", "Rojo")
print(perro2.velocidad(20))

perro3 = Perro("Canis familiarrrris", "Canidaesss", "Azul")


gato = Gato("Felis catus", "Felidae", "Cafe")
print(gato.velocidad(5))
print(perro)
print(perro2)
print(perro3)
ambos = perro + perro2 + perro3
print(ambos)
