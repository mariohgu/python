
def is_armstrong_number(number):
    lena = int(len(str(number)))
    print(lena)
    suma = sum([int(i)**lena for i in str(number)])
    if number == suma:
        return True
    return False

print(is_armstrong_number(154))