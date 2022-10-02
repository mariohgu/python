from itertools import chain


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
        'position': 'Support',
        'language': '',
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

def run():
    #como lisst comprehension
    trabajadores_platzi = [worker["name"] for worker in DATA if worker["language"]=="python"]
    #como functions highorder
    edadWorker = list(filter(lambda worker: worker["age"]>18,DATA))
    edadWorker = list(map(lambda worker:worker["name"],edadWorker))
    #agregando un termino al diccionario.
    edadIncluida = list(map(lambda worker: worker | {"old":worker["age"]>70},DATA))
    #mostrando dos valores desde diccionario
    nombre_edad = list((chain.from_iterable((worker['name'],worker['age']) for worker in DATA if worker['age']>30)))
    #map para agregar exponentes a la listas
    nombre_edad = list(map(lambda x: x**2 if type(x)==int else x,nombre_edad))

    lenguaje = list(filter(lambda filtro:filtro['language']=='python',DATA))

    print (lenguaje)
    print(edadWorker)
    print(nombre_edad)
    for worker in trabajadores_platzi:
        print(worker)

if __name__ == '__main__':
    run()