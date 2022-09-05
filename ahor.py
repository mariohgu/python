
word = "martillo"

arrayword=list(word)
miWord=["_" for i in range(len(word))]
#muestraWord = (lambda a:a for a in arrayword)
print(arrayword)
print(miWord)
attemp:int = 0
while miWord!=arrayword:
    if attemp==6:break
    chare = input('Dame la letra: ')
    if chare in arrayword:
        for i,n in enumerate(arrayword):
            if chare==n:
                miWord[i]=chare
                print(miWord)
    else:
        attemp +=1
        print(f'no es correcto tienes {6-attemp} oportunidades' if attemp<6 else f'INTENTALO DE NUEVO')

if arrayword==miWord:
    print("LO LOGRASTE")


        
    


