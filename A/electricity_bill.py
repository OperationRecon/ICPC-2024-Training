x = int(input())
end_of_month = {0:10,1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
while x:
    consec = 0
    power = 0
    nd,nm,ny,np = (0,0,0,0)
    d,m,y,p = nd+1,nm+1,ny+1,np+1
    for i in range(x):
        z = input().split()
        d,m,y,p = nd,nm,ny,np
        nd,nm,ny,np = [int(x) for x in z]
        if m == 2:
            if not ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
                if d == 28 and nd == 1 and nm == 3 and y == ny:
                    consec += 1
                    power += (np - p)
                    continue
        
        if d + 1 != nd:
            if d == end_of_month[m] and nd == 1:
                m += 1
            else: 
                continue
        
        if m != nm:
            if m == 13 and nm == 1:
                y += 1
            else:
                continue
        
        if y != ny:
            continue

        consec += 1
        power += (np - p)


    print(consec,power)
    x = int(input())

