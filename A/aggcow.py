import bisect

def get_closest_below(start,end,l,v):
    mid = int((start+end)/2)
    while start < end:
        mid = int((start+end)/2)
        if v == l[mid]:
            return mid
        elif v > l[mid]:
            if start == mid:
                return mid
            start = mid
        else:
            end = mid - 1
    return mid

def get_closest_above(start,end,l,v):
    mid = int((start+end)/2)
    while start < end:
        mid = int((start+end)/2)
        if v == l[mid]:
            return mid
        elif v > l[mid]:
            start = mid + 1
        else:
            if end == mid:
                return mid
            end = mid
    return mid

t = int(input())
for i in range(t):
    n,c = [int(x) for x in input().split()]
    p = list()
    for _ in range(n):
        pos = int(input())
        bisect.insort_left(p,pos)

    occupied = []
    min_max = -1
    for k in range(c):
        if k == 0:
            occupied.append(0)
            continue
        elif k == 1:
            occupied.append(n-1)
            min_max = abs(p[occupied[0]]-p[occupied[1]])
            continue

        max_dst = 0
        current_place = -1
        for j in range(len(occupied)-1):
            if occupied[j] == occupied[j+1]-1:
                continue
            avg = (p[occupied[j]]+p[occupied[j+1]])/2

            x,y = (get_closest_below(occupied[j]+1,occupied[j+1]-1,p,avg)),(get_closest_above(occupied[j]+1,occupied[j+1]-1,p,avg))

            if x == min(abs(p[x]-avg),abs(p[y]-avg)):
                possible_place = x
            else:
                possible_place = y
            dst = min(abs(p[possible_place]-p[occupied[j]]),abs(p[possible_place]-p[occupied[j+1]]))
            if dst > max_dst:
                max_dst = dst
                current_place = possible_place

            if max_dst == 1:
                 break
        
        bisect.insort_left(occupied,current_place)
        min_max = max_dst

    print(min_max)


        
    
