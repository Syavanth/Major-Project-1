def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 36
b = 60


result = gcd(a, b)
print(result)  
