# S: Single Responsability Principle: Una clase debe tener una sola responabilidad
# responsabilidad unica, una clase debe tener una sola responsabilidad. No hay sobrecarga, es decir que tenga muchas funciones. Es importante que saber que esa clase puede hacer su tarea sin depender de otra clase.
# ejemplo: una clase para manejar la base de datos de un programa de gestión de tareas,
# solo debe tener una responsabilidad: manejar la base de datos.
# no debe tener funciones para mostrar la interfaz gráfica, ni funciones para
# enviar notificaciones, ni funciones para guardar los datos en un archivo, etc.


class Auto:
    def __init__(self, tanque):
        self.tanque = tanque
        self.posicion = 0

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.disminuir_combustible(distancia / 2)
            print("se movio el auto")
        else:
            print("No me puedo mover")

    def obtener_posicion(self):
        return self.posicion


class TaquedeCombustible:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.combustible = 100

    def obtener_combustible(self):
        return self.combustible

    def disminuir_combustible(self, litros):
        self.combustible -= litros

    def agregar_combustible(self, litros):
        self.combustible += litros


tanque = TaquedeCombustible(100)
auto = Auto(tanque)

auto.mover(50)
print(auto.obtener_posicion())

auto.mover(40)
print(auto.obtener_posicion())

auto.mover(200)
print(auto.obtener_posicion())
