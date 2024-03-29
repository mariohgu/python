from functools import reduce


def run():
    numList = [1, 2, 3, 4]

    square = list(map(lambda x: x**2, numList))  # [i**2 for i in numList]
    mult = reduce(lambda a, b: a * b, numList)
    print(square)
    print(mult)

    class Empleado:
        def __init__(self, nombre, cargo, sueldo):
            self.nombre = nombre
            self.cargo = cargo
            self.sueldo = sueldo

        def __repr__(self) -> str:
            return str(
                f"{self.nombre} tiene el cargo de {self.cargo} y recibe {self.sueldo} dolares"
            )

    listaEmpleados = [
        Empleado("Mario", "CEO", 50000),
        Empleado("Jhon", "CTO", 40000),
        Empleado("Dolly", "CMO", 30000),
    ]

    Carlos = Empleado("Carlos", "CFO", 100000)
    print(min(listaEmpleados, key=lambda x: x.cargo))
    print(Carlos)
    print(listaEmpleados)


if __name__ == "__main__":
    run()
