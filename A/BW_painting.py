while True:
    y = input()
    if y == '0 0 0':
        break

    n,m,c = [int(x) for x in y.split()]

    white = 0

    for i in range(m-7):
        if n % 2 == 0:
            white += (n-8)//2+c
        else:
            white += (n-8)//2+1
        c = not c
        
    print(white)


