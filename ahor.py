"""
incorpora comprehensions, manejo de errores y manejo de archivos.
utiliza el data
funcion enumerate
metodo get de los diccionarios puede servirte
sentencia("cls") limpiar pantalla
añade puntos
dibujar al ahorcado
mejorar interfaz.
"""

import os
from random import randint


def figure(argument):
    switcher = {
        0: " ",
        1: """ 
               |
            ___|___
                
            """,
        2: """
                |      
                |     
                |
            ____|___                     
            
            
            """,
        3: """
        
                _______
                |/      
                |      
                |
            ____|___
        
        
            """,
        4: """
        
                 _______
                |/      |
                |      (_)
                |      
            ____|___
                    
        
        """,
        5: """
        
                 _______
                |/      |
                |      (_)
                |      \|/
                |      
                |      
            ____|___
        
        """,
        6: """
                 _______
                |/      |
                |      (_)
                |      \|/
                |       |
                |      / 
                |
            ____|___  YOUR ARE DEAD
                    
        """,
    }
    return switcher.get(argument, "nothing")


def loadWord():
    word = ["camion", "perro", "murcielago"]
    # with open("./files/data.txt","r",encoding="utf-8") as f:
    #     for line in f:
    #         word.append(line)
    chooseWord = word[randint(0, len(word))].rstrip("\n")
    listWord = list(chooseWord)
    playerWord = ["_" for i in range(0, len(chooseWord))]
    attp = 0
    while listWord != playerWord and attp < 6:
        lett = input("           Please, give me a letter: ")
        if lett not in playerWord:
            for i, j in enumerate(chooseWord):
                if j == lett:
                    playerWord[i] = j
            os.system("cls")
            if lett not in playerWord:
                attp += 1
            print(figure(attp))
            for s in playerWord:
                print(s, end=" ")
        else:
            print("\nYou are right, but you already used that letter.")
    if attp == 6:
        print("\nQUEMASTE", " The word was", chooseWord)
    else:
        print("\nLO LOGRASTE")


def run():
    loadWord()


if __name__ == "__main__":
    run()
