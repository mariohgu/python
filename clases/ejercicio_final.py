class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def liberar(self):
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            print("Se ha reservado la habitacion")
            self.ocupada = True
            return True
        else:
            print("La habitacion ya se encuentra ocupada")
            return False


class Hotel:

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, numero, tipo, precio):
        habitacion = Habitacion(numero, tipo, precio)
        self.habitaciones.append(habitacion)

    def disponibilidad(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.ocupada and habitacion.numero == numero:
                return False
        return True

    def reservar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if not habitacion.ocupada:
                    habitacion.reservar()
                    return f"La habitacion {habitacion.numero} ha sido reservada"
                else:
                    return (
                        f"La habitacion {habitacion.numero} no se encuentra disponible"
                    )
        return f"La habitacion {numero} no existe"

    def liberar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                if habitacion.ocupada:
                    habitacion.liberar()
                    return f"La habitacion {habitacion.numero} ha sido liberada"
                else:
                    return f"La habitacion {habitacion.numero} no se encuentra ocupada"
        return f"La habitacion {numero} no existe"


hotel_principal = Hotel("Grand Hotel", "Av. Siempre Viva 123")
hotel_principal.agregar_habitacion(101, "estandar", 100)
hotel_principal.agregar_habitacion(102, "suite", 200)


print(hotel_principal.reservar_habitacion(101))
print(hotel_principal.liberar_habitacion(101))
