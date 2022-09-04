def line(string:str) -> str:
    assert type(string)==str,"no es string"
    def quatity(a:int):
        return a*string
    return quatity

def make_division_by(x:int)-> float:
    return lambda n:x/n

def run():
    cual = line("hola ")
    print(cual(4))
    
    divis = make_division_by(5)
    print(divis(2))

if __name__ == '__main__':run()
    