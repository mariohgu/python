def divisor(num):
    dved = [i for i in range (1,num+1) if num%i==0]
    return dved
    

def run():
    while True:
        try:
            x = int(input("Ingrese numero: "))
            if x<1:
                raise ValueError
            print(divisor(x))
            break            
        except ValueError:
            print("Error de dato")

if __name__ == '__main__':run()