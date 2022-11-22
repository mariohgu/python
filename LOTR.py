'''
/*
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
 */
 '''
 
 
 
tipos = [
    
    {
        "Tipo":"AGUA",
        "FUEGO":2,
        'PLANTA':0.5,
        'ELECTRICO':1,
        'AGUA':0.5,
        
    },
    {
        'Tipo':'FUEGO',
        "AGUA":0.5,
        'PLANTA':2,
        'ELECTRICO':1,
        'FUEGO':0.5,
        
    },
        {
        'Tipo':'PLANTA',
        "AGUA":2,
        'PLANTA':0.5,
        'ELECTRICO':1,
        'FUEGO':0.5,
        
    },
        {
        'Tipo':'FUEGO',
        "AGUA":0.1,
        'PLANTA':4,
        'ELECTRICO':9,
        'FUEGO':0.3,
        
    },
        {
        'Tipo':'ELECTRICO',
        "AGUA":2,
        'PLANTA':0.5,
        'ELECTRICO':0.5,
        'FUEGO':1,
        
    }
]

nombre = list(filter(lambda x:x['Tipo']=='FUEGO',tipos))
numero = list(map(lambda num:num['AGUA'],nombre))
print(nombre)
print(numero)

#if __name__=='__main__':run()
 
 
 
 
 