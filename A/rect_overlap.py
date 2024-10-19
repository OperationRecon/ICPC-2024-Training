t = int(input())

for i in range(t):
    _ = input()
    x1ll,y1ll,x1ur,y1ur = [eval(x) for x in input().split()]
    x2ll,y2ll,x2ur,y2ur = [eval(x) for x in input().split()]

    xll = max(x1ll,x2ll)
    xur = min(x1ur,x2ur)

    yll = max(y1ll,y2ll)
    yur = min(y1ur,y2ur)

    if i > 0:
        print()

    if xll >= xur or yll >= yur:
        print('No Overlap')
        continue

    print(xll,yll,xur,yur)

