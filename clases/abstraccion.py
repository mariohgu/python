class Auto:
    def __init__(self):
        self.__estado = "apagado"

    def encender(self):
        self.__estado = "encendido"

    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("Voy a conducir")


mi_auto = Auto()
mi_auto.conducir()
