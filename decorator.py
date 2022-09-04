def name(func):
    def envoltura(nam: str):
        return func(nam).upper()
    return envoltura

@name
def nombre(name):
    return f'{name}, tienes mensaje'


def change(func):
    def wrapper(*args,**kwargs):
        print("some code")
        func(*args,**kwargs)
        print("other code")        
    return wrapper

#TypeError: suma() missing 1 required positional argument: 'b'
def modifi(func):
    def wrapper(a:int,b:int):
        func(a,b)
        x:int = func(a)-1
        y:int = func(b)-1
        print(f'y la multiplicacion es {x*y}')
    return wrapper
        

@modifi
def suma(a:int,b:int):
    #print(f'la suma es {a+b}')
    return f'la suma es {a+b}'
    



print(nombre("Mario"))
suma(3,4)