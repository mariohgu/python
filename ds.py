from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from typing import Optional

class Status(Enum):
    HIRED = auto()
    CESADED = auto()
    
@dataclass
class Person(ABC):
    DNI:int
    name:str
    birth_year: datetime
    
    @abstractmethod
    def __str__(self) -> str:
        return super().__str__()


@dataclass  
class Employee (Person):
    status: Status
    area: str
    commision:Optional[float] = None
    email: Optional[list] = field(default_factory=list)
    id:str = field(default_factory=str)
    
    def __post_init__(self):
        self.birth_year = self.birth_year[-4:]
               
    
    def __str__(self) -> str:
        return f'{self.DNI},hola {self.name}, {self.birth_year}, {self.status.name}, {self.area}'

@dataclass
class Gerencia(Employee):
    
    sueldo:int = field(default_factory=int)
    dia_reunion:datetime.date =field(default_factory=str)
    
    def __str__(self) -> str:
        #super().__str__()
        return f'{self.name} es gerente con dni {self.DNI} y tiene un sueldo de {self.sueldo} y trabaja los dias {self.dia_reunion}'

lista = list(filter(lambda x:x%2==0, range(0,100)))
lista2  = list(map(lambda x : x**2, range(0,10)))
print(lista)
print(lista2)
print()

mario = Employee(44444,"mario","31/08/1984",Status.HIRED,"IT")
doris = Gerencia(DNI=5555,name= "doris",birth_year="15/04/1952",status=Status.HIRED,area="Gerencia",commision= 1400,id="wwww",sueldo= 6511111,dia_reunion="martes")
#print (f'{mario.name} pertence al area de {mario.area} y nacio {mario.birth_year}, su estado actual es {mario.status.name} y su comisiion es {mario.commision}')
print(mario)
print(doris)


    
    
    