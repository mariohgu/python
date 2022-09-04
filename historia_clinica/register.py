from dataclasses import dataclass
from enum import Enum,auto
from datetime import datetime



class statePatient(Enum):
    ACTIVE = auto()
    NO_ACTIVE = auto()

class hemoglobina(Enum):
    ALTA,MEDIA,BAJA=range(3)
    
@dataclass
class Patient:
    names:str
    dni:int
    state:statePatient
    year:int
    hematoma:hemoglobina
    
    def tiempo_dialisis(self)->int:
        return datetime.now().year-self.year
    
    def show_data(self) -> str:
        return "revisar urgente" if self.hematoma==0 and self.tiempo_dialisis() else "no revisar"
    
class showoff:
    names:str
    year:int
    def imprimir (self):
        return(f'el año es {self.year} y el nombre es {self.names}')

class Centro:
    def __init__(self) -> None:
        self.patients_dialisis:list[Patient]=[]
    
    def patient_register(
        self,
        names:str,
        dni:int,
        state:statePatient,
        year:int,
        hematoma:hemoglobina
        
    ) -> None:
        self.patients_dialisis.append(Patient(names,dni,state,year,hematoma))
    
    def imprimir(self):
        showoff()


def run():
    registros= Centro()
    registros.patient_register("Esteban",454545,statePatient.ACTIVE,2018,hemoglobina.ALTA)
    print(registros)
    


if __name__ =="__main__":run()
    
    
        
        
    

