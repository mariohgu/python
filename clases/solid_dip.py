# D: Dependency Inversion Principle: Las clases deben depender de abstracciones, no de implementaciones concretas.
# Esto se logra a de la creación de abstracciones y la inversión de dependencias.
# Por ejemplo, en lugar de que una clase dependa de una implementación concreta de un servicio,
# se crea una interfaz o clase abstracta que define el contrato que debe cumplir cualquier implementación.
# Luego, la clase que depende de esa interfaz o clase abstracta no depende de una implementación concreta,
# sino que depende de la interfaz o clase abstracta.
# De esta manera, si se cambia la implementación concreta del servicio, la clase que depende de la interfaz
# o clase abstracta no necesita cambiar, ya que sigue dependiendo de la interfaz o clase abstracta.

from abc import ABC, abstractmethod


class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, texto):
        pass


class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, texto):
        pass


class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        pass


corrector = CorrectorOrtografico(Diccionario())
corrector.corregir_texto("hola")

corrector_web = CorrectorOrtografico(ServicioWeb())
corrector_web.corregir_texto("hola")
