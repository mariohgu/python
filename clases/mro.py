class Animal:
    def comer(self):
        print("estoy comiendo")


class Mamifero(Animal):
    def amamantar(self):
        print("estoy amamantando")


class Ave(Animal):
    def volar(self):
        print("estoy volando")


class Murcielago(Mamifero, Ave):
    pass


murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())
