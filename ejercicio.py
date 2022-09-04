
# def func(a:int, b:int, c:int)-> int:
#     return max(a,b,c)

# print(func(19,15,25))

# def vowel(word:str)-> bool:
#     if word in 'aeiou':
#         return True
#     else:
#         return False

# print(vowel('b'))

# def arit(lst: list):
#     a = sum(lst)
#     b = 1
#     for i in lst:
#         b = b*i
#     print (a,b)
    

# arit([8,2,3,4])
    
# def inversa (word:str)->bool:
#     word = word.lower().replace(" ","")
#     return word[::-1]==word

# print(inversa("radart"))

# def esta(lst1: list, lst2: list)-> bool:
#     for num_a in lst1:
#         if num_a in lst2:
#             return True

#     return False

# print(esta([1,2,3,4], [4,7,8,9]))

# def impr(lst1: list):
#     for a in lst1:
#         print(a*"*")

# impr([2,6,9])




# def filtrar(lst1:list,n:int)-> list:
#     lst2:list=[]
#     for ls in lst1:
#         if len(ls)>n:
#             lst2.append(ls)
#     return lst2

# def filtrar(lst: list):
#     b=0
#     c=""
#     for ls in lst:
#         if len(ls)>b:
#             b=len(ls)
#             c=ls
#     return c

# print(filtrar(["hol","riadasdaddad","22","qeqw","erttttttttttttttttttttttttttttttttttttttpa"]))



# def cadena(word:str)->int:
#     c=0
#     for i in word:
#         if i.isupper():
#             c+=1
#     return c
        
# print(cadena("MaRio"))

# from typing import BinaryIO
# def bina(num:BinaryIO)->int:
#     return int(num)

# print(bina(0b1001))

def nombres(name: dict):
    anio=int(input("año en curso: "))
    for i in range(3):
        nam = input(f'Ingrese el nombre del numero {i+1}: ')
        edad = int(input(f'Ingrese el año de nac de {i+1}: '))
        name[nam]=edad
    
    for i in name:
        print(f'{i} tendra {anio-name[i]} en el {anio}')
    
    # for ind,names in enumerate(names):
    #     print(f'{name[ind]} tendra {anio-names}')

nombres({})