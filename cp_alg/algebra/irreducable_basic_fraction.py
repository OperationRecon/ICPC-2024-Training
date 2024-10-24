from math import sqrt
def phi(n):
    res = n
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            res -= res // i
    if n > 1:
        res -= res // n
    return int(res)

n = int(input())

while n != 0:
    print(phi(n))
    n = int(input())

    
