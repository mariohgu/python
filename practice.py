from ast import Str
from dataclasses import dataclass
from enum import Enum
from typing import Optional


def search_str(string:str):
    lower_case=[x for x in string if x.islower()]
    upper_case = [y for y in string if y.isupper()]
    print(f'The lowercases are: {lower_case} and \nthey are: {len(lower_case)}')
    print(f'The uppercases are {upper_case} and \nthey are: {len(upper_case)}')

def hiy(hey:str):
    return "ya" if hey=="r" else "no"

class Tipos(Enum):
    HARDWARE,SOFTWARE,PERIFERICO = range(3)

@dataclass
class Inventario():
    
    tipo_venta:Tipos
    codigo:int
    precio:int
    descripcion:Optional[str]=None
    
    
    def __post_init__(self):
        assert len(str(self.codigo))!=5,"Favor de revisar que el codigo sera de 5 digitos"
        
    def __str__(self) -> str:
        return f"El codigo es: {self.codigo} de tipo de {self.tipo_venta.name}, de precio {self.precio}, detallando en {self.descripcion}"
    
    
    

def run():
    search_str("Welcome to the World of Possibilities!")
    print(hiy("uu"))
    mouse = Inventario(tipo_venta=Tipos.PERIFERICO, codigo=742594,precio=15)
    print(mouse)



if __name__ == '__main__':run()