from dataclasses import dataclass
from datetime import datetime
from enum import Enum,auto

class Estado(Enum):
    ACTIVO=auto()
    DESACTIVO=auto()
    
@dataclass
class Paciente:
    nombres:str
    dni:int
    estado:Estado
    year: int=datetime.now().year
    
    def __str__(self) -> str:
        return f'todo ok con {self.nombres} con dni {self.dni} con año {self.year} y de tipo {self.estado.name}'
    
    def __post_init__(self) -> None:
        assert len(self.dni)==7,"REVISAR QUE DNI TIENE 7 DIGITOS"
    

paciente1 = Paciente("mario",454545,Estado.ACTIVO,2011)
print(paciente1)
    