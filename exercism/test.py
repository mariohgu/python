import secrets
def private_key(p):
    if p<1:
        raise ValueError("Number can not be least than 1")
    x = [i for i in range(2,p) if all(i%j for j in range(2,min(i,11)))]
    c = secrets.choice(x)
    return c  

def public_key(p, g, private):
    p = private_key(p)
    g = private_key(g)
    a = secrets.choice(range(2,private))
    A = (pow(g,a,p))
    return A

def secret(p, public, private):
    S = public_key(p,public,private)
    return S

print(secret(23,5,6))

# p = private_key(300)
# g = private_key(200)

# a = secrets.choice(range(2,18))
# b = secrets.choice(range(2,3))


# A = (pow(g,a))%p
# B = (pow(g,b))%p

# S = (pow(B,a))%p
# H = (pow(A,b))%p

# if S==H:
#     print('yep')
# else:
#     print('nop')


