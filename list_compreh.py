def run():
    dictio = {
        i : i**2 for i in range(0,10) if i%3 != 0
    }
    print(dictio)
    
    palindrome = lambda word:word==word[::-1]
    print(palindrome('ana'))
    
#    square = [i**2 for i in range(0,100) if i%3!=0]
#    print(square)

if __name__ == '__main__':
    run()