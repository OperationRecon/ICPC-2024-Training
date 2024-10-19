t = int(input())
for i in range(t):
    x = int(input())
    sides = (2/((180-x)/180))
    if sides%1 == 0:
        print('YES')
    else:
        print('NO')