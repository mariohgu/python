# L: Liskov Substitution Principle: Los hijos deben ser sustitutos perfectos de sus padres
# nos dice que las clases hijas deben hacer lo mismo que las clases padres, es decir si tenemos una clase Ave, tenemos que tener comportamientos que todas las aves puedan hacer. Por ejemplo el pinguino es un ave pero no puede volar, entonces tenemos que tener presente eso.

# I: Interface Segregation Principle: No se debe forzar a las clases a implementar metodos que no usan.
# Es decir, una clase no debe tener que implementar un método que no va a usar.
# Si una clase no va a usar un método, no debe tener que implementarlo.
# Esto ayuda a mantener la cohesión y la responsabilidad de cada clase.

from abc import ABC, abstractmethod


class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador):
    def trabajar(self):
        print("Trabajando")

    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("Robot Trabajando")

    def comer(self):
        print("Robot Comiendo")

    def dormir(self):
        print("Robot Durmiendo")


"""
Como podemos ver hemos implementando clases abstractas que no son necesarias para ciertos objetos. Por ejemplo Robot, no deberia comer y dormir
por lo que es importante revisar en detalle que es lo que se necesita para cada clase.
"""
