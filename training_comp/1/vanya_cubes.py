
n = int(input())
i = 1
req = 1
while n >= req:
    i += 1
    req += (i*(i+1))//2


print(i-1)