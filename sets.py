from typing import Dict, List

positives: List[int] = [1,2,3,4]
diction:Dict[str,int]={
    "Hola":123,
    "Dos":456
}

def remove_duplicate(lista: list)->list:
    new_list=[]
    for elem in lista:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

def short_remove(lista:list)-> list:
    return list(set(lista))

print(remove_duplicate([2,2,5,3,3,8,6]))
print(short_remove([2,2,5,3,3,8,6]))
new_lista = lambda x:list(set(x))
print(new_lista([2,2,5,3,3,8,6]))