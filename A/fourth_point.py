
while True:
    try:
        x1,y1,x2,y2,x3,y3,x4,y4 = [float(x) for x in input().split()]
        if (x3,y3) not in ((x1,y1),(x2,y2)):
            x3,y3,x4,y4 = x4,y4,x3,y3
        
        if (x1,y1) != (x3,y3):
            x2,y2,x1,y1 = x1,y1,x2,y2
        vec1 = (x2-x1,y2-y1)
        forth_point = (vec1[0]+x4,vec1[1]+y4)
        print(f'{forth_point[0]:.3f}',f'{forth_point[1]:.3f}')
    except:
        break