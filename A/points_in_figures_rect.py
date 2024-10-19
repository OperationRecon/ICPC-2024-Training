rects = []
for i in range(10):
    ln = input().split()
    if ln[0] == '*':
        break
    for j in range(1, 5):
        ln[j] = eval(ln[j])
    rects.append(((ln[1],ln[2]),(ln[3],ln[2]),(ln[3],ln[4]),(ln[1],ln[4])))

p = [eval(x) for x in input().split()]
n = 1

while  not(p[0] == p[1] and p[0] == 9999.9):
    not_contained = True
    for i in range(len(rects)):
        inside = True
        for j in range(4):
            vec_p = (p[0]-rects[i][j][0],p[1]-rects[i][j][1])
            vec_ln = (rects[i][(j+1)%4][0]-rects[i][j][0],rects[i][(j+1)%4][1]-rects[i][j][1])
            crs = (vec_p[0]*vec_ln[1]-vec_p[1]*vec_ln[0])
            if crs <= 0:
                inside = False
                break

        if inside:
            print(f'Point {n} is contained in figure {i+1}')
            not_contained = False

    if not_contained:
        print(f'Point {n} is not contained in any figure')
    
    n += 1
    p = [eval(x) for x in input().split()]

        
