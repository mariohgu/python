# O: Open/Closed Principle: La clase debe estar abierta a extensiones, pero cerrada a modificaciones


class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def notificar(self):
        print(
            f"notificando por email a {self.usuario.email} con el siguiente mensaje: {self.mensaje}"
        )


class NotificadorSMS(Notificador):
    def notificar(self):
        print(
            f"notificando por SMS a {self.usuario.telefono} con el siguiente mensaje: {self.mensaje}"
        )


class NotificadorCarta(Notificador):
    def notificar(self):
        print(
            f"notificando por carta a {self.usuario.direccion} con el siguiente mensaje: {self.mensaje}"
        )


# En este ejemplo vemos que usuario es un objeto que recibira luego la clase Notificador. El objeto usuario tiene ciertas caracteristicas que cada clase hija de notificador aprovecharan para ejecutar su tarea. Aqui podemos ver que cumplimos el principio de abierto/cerrado, ya que no estamos moficando la clase Notificador sino implementando mas clases.
