from sympy import isprime
a=0
dknl = []
while True:
    if isprime(a)==True:
        b = (2**a -1)
        if isprime(b) == True:
            print(2**(a-1)*b)
        a+=1
    else:
        a+=1
