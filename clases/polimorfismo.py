# polimorfismo de sobrecarga de metodos, es cuando declaras un metodo parametro se comporta de una forma y cuando pasas otros parametros tiene otro comportamiento. Esto es habitual en java
"""
class Escribe:
    def escribir(nombre):
        print(f'Hola {nombre}')
    
    def escribir(nombre, apellido):
        print(f'Hola {nombre} {apellido}'

"""
# polimorfismo de cohesion, es cuando a pesar de tener distintos tipos de datos, la implementacion no varia

"""
num1=2 (int)
num2=3.4 (float)
numero = num1+num2 (float)
"""

# duck typing, enlaces dinamicos y estaticos, tipo real y declarado.

# duck typing, enlaces dinamicos y estaticos, tipo real y declarado.
# tipo real: es el tipo que tiene una variable en el momento de la ejecución
# tipo declarado: es el tipo que se le asigna a una variable en el momento de su declaración
# enlace dinamico: se hace en tiempo de ejecución, el compilador no sabe que tipo es
# enlace estático: se hace en tiempo de compilación, el compilador sabe que tipo es

# tipo real: es el tipo que tiene una variable en el momento de la ejecución


# tipo real: es el tipo que tiene una variable en el momento de la ejecución
real: int = 2
print(type(real))  # <class 'int'>

# tipo declarado: es el tipo que se le asigna a una variable en el momento de su declaración
declared: str = "hola"
print(type(declared))  # <class 'str'>


# enlace dinamico: se hace en tiempo de ejecución, el compilador no sabe que tipo es
# enlace estático: se hace en tiempo de compilación, el compilador sabe que tipo es

dinamico = "hola"
print(type(dinamico))  # <class 'str'>

estatico: str = "hola"
print(type(estatico))  # <class 'str'>
