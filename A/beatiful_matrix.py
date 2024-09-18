x,y = (0,0)
for i in range(5):

    row = input()
    if '1' in row:
        x = i + 1
        y = row.index('1')//2+1
        print(abs(x-3)+abs(y-3))
