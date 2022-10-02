from itertools import chain
from dataclasses import dataclass,field
from enum import Enum
from typing import Optional


class Tipo(Enum):
    AGUA,FUEGO,TIERRA,ELECTRICO = range(4)
    

@dataclass
class Pokemon():
    name:str
    ataque:int
    defensa: int
    tipo: Tipo
    region:Optional[str]=field(default='johto')

    
    def enojado(self)->int:
        return self.ataque*2
    
    #def __post_init__():
    #    pass    


squirtle = Pokemon(name='squirtle',ataque=330,defensa=500,region='lavanda',tipo=Tipo.AGUA)
charmander = Pokemon(name='charmander',ataque=350,defensa=400,tipo=Tipo.FUEGO)
atqsqui = squirtle.__dict__['ataque']
print(atqsqui)
print(squirtle.enojado())
print(squirtle)    
print(charmander)

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Student',
        'language': 'php',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

list_student = list(chain.from_iterable((work['name'],work['age']) for work in (filter(lambda obje:obje['position']=='Student',DATA))))
list_name_student = [work['name'] for work in DATA if work['position']=='Student']
print(list_student)
print(list_name_student)