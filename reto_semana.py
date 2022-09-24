'''
/*
 * Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! 
 * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
 * "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
 * que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento 
 *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
 */
 '''
 
# from datetime import date
# import math

# def date_dif(date_play:date.fromisoformat)-> str:
#     date_tof=date.fromisoformat('2023-05-12')
#     diferencia = date_tof-date_play
#     dif_anio=math.floor(diferencia.days/365)
#     dif_days = round(diferencia.days%365)
#     print (f'Faltan {dif_anio} años con {dif_days} dias')

# date_dif(date.fromisoformat('2021-08-10'))



'''
/*
 * Enunciado: Crea un programa se encargue de transformar un número binario
 * a decimal sin utilizar funciones propias del lenguaje que 
 * lo hagan directamente.
 */'''
 


def a_dec(num:str):
    s = 0
    num = list(num)
    for i in range(len(num)):
        j = num.pop()
        if j == '1':
            s = s + pow(2,i)
    print(s)
#     list_num =list(num)
#     suma = 0
    
#     for valor in range(len(list_num)):
#         numero = list_num.pop()
#         if numero =='1':
#             suma = suma + pow(2,valor)

#     print(suma)





def nombre(namex:str):
    nuevo = namex[:namex.find('@')]
    nuevo = nuevo+'@ceu.es'
    
    
    print(nuevo)
    



def run():
    
   # n = input("Dame tu nombre: ")
    #nombre(n)
    a_dec('01110')

    # a = [1,2,4,5]
    # b = a.copy()
    # b = [7,8,9,7]
    # print (a,b)

    
 
if __name__ == '__main__':run()