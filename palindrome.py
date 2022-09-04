

def palindrome(a: str) -> bool:
    a = a.replace(" ","").lower()
    return a==a[::-1]

def prime(a:int)-> bool:
    es = [x for x in range(1,a+1) if a%x==0]
    return len(es)<=2


def run():
    print(palindrome("ana"))
    print(prime(7))
    
if __name__ == '__main__':run()
        