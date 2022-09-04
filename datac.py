from enum import Enum,auto
from dataclasses import dataclass
from time import sleep
from typing import Optional

class Tipo(Enum):
    ELECTRICO = auto()
    MECANICO = auto()

@dataclass
class Auto():
    placa:int
    tipo:Tipo
    ruedas: Optional[int] = None
    lugar:str="Pohang"
    
    def __str__(self) -> str:
        return f'la placa es {self.placa} del tipo {self.tipo.name} con {self.ruedas} ruedas y del estado de {self.lugar}'


def fibo(num:int=None):
    x1=0
    x2=1
    
    while True:
        if not num or num>x1:
            yield x1
            x1, x2 = x2, x1+x2            
        else:
            break

def run():
    nuevoCar=Auto(454444,Tipo.ELECTRICO)
    print(nuevoCar)
    hola=fibo(88)
    for x in hola:
        print (x)
        sleep(1)



if __name__ == "__main__":
    run()
        
    