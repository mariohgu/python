mylist = [1,3,6,2,8,67,53,44,98,79]
print(mylist)

odd = list(filter(lambda x:x%2!=0,mylist))
print(odd)

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self) -> str:
        return f'{self.nombre} tiene el cargo de {self.cargo} y recibe {self.salario} dolares'

listaEmpleados = [
    Empleado("Mario","CEO",50000),
    Empleado("Jhon","CTO",40000),
    Empleado("Dolly","CMO",30000)
]
dato = 35000
minEmpleado = filter(lambda x:x.salario>dato,listaEmpleados)
for salario_alto in minEmpleado:
    print(salario_alto)