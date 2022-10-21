def square(number):
    if not 1<=number<=64:
        raise ValueError ("square must be between 1 and 64")
    return pow(2,(number-1))

number = int(input("dame n: "))
print(square(number))

#numeros primos
num3 = [x for x in range(2, 1010) if all(x%y for y in range(2, min(x, 11)))]