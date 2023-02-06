#try-except
lens = "quiero lentes"
try:
    lens2 = int(lens)
except:
    lens2 = -1

print(lens2)

dame = input("dame un numero")
try:
    dame = int(dame)
except:
    dame = -1

if dame == -1:
    print("no es un numero")
else:
    print("el numero correcto")

####EJERICICIOS#####

hours = int(input("Ingrese las horas trabajadas: "))
horario = lambda x: x*1 if x<=40 else ((x-40)*1.5)+((x-(x-40))*1.0)
dos = horario(hours)
print(dos)



