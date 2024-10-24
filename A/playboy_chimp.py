global l,n

def get_shorter(start,end,h):
    mid = int((start+end)/2)
    if start >= end:
        if l[mid] >= h:
            return 'X' if mid <= 0 else l[mid-1]
        else:
            return l[mid]
    
    elif l[mid] >= h:
        return get_shorter(start,mid-1,h)
    else:
        return get_shorter(mid+1,end,h)

def get_taller(start,end,h):
    mid = int((start+end)/2)

    if start >= end:
        if l[mid] <= h:
            return 'X' if mid >= n-1 else l[mid+1]
        else:
            return l[mid]
    
    elif l[mid] > h:
        return get_taller(start,mid-1,h)
    else:
        return get_taller(mid+1,end,h)


def get_partners(start,end,h):
    return get_shorter(start,end,h), get_taller(start,end,h)


n = int(input())
l = [int(x) for x in input().split()]
q = int(input())
hs = [int(x) for x in input().split()]

for h in hs:
    t,s =get_partners(0,n-1,h)
    print(t,s)