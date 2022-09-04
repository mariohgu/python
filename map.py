from functools import reduce


def run():
    numList=[1,2,3,4]
    
    square = list(map(lambda x: x**2,numList)) #[i**2 for i in numList]
    mult = reduce(lambda a,b:a*b,numList)
    print(square)
    print (mult)
    
    class Empleado:
        def __init__(self,nombre,cargo,sueldo):
            self.nombre = nombre
            self.cargo = cargo
            self.sueldo = sueldo
        
        def __str__(self):
            return f'{self.nombre} tiene el cargo de {self.cargo} y recibe {self.salario} dolares'
    
    listaEmpleados = [
    Empleado("Mario","CEO",50000),
    Empleado("Jhon","CTO",40000),
    Empleado("Dolly","CMO",30000)
    ]



if __name__ == '__main__':
    run()
