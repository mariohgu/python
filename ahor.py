
word = "Martillo"

arrayword=list(word)
miWord=["_" for i in range(len(word))]
#muestraWord = (lambda a:a for a in arrayword)
print(arrayword)
print(miWord)

while miWord!=arrayword:
    chare = input('Dame la letra')
    for i,n in enumerate(arrayword):
        if chare==arrayword[i]:
            miWord[i]=chare
            print(miWord)
            

print("final")
        
    


