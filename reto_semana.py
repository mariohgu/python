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
 
from datetime import date
import math

def date_dif(date_play:date.fromisoformat)-> str:
    date_tof=date.fromisoformat('2023-05-12')
    diferencia = date_tof-date_play
    dif_anio=math.floor(diferencia.days/365)
    dif_days = round(diferencia.days%365)
    print (f'Faltan {dif_anio} años con {dif_days} dias')

date_dif(date.fromisoformat('2021-08-10'))
    
    