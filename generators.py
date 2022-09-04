from time import sleep

def fibo_gen(max:int=None):
    assert type(max)==int, "ERROR: Max must be an integer"
    n1 = 0
    n2 = 1
    
    while True:
        if not max or max>n1:
            yield n1
            n1, n2 = n2, n1+n2
        else:
            break

if __name__ == "__main__":
    fibo = fibo_gen(25)
    for elem in fibo:
        print(elem)
        sleep(1)
        