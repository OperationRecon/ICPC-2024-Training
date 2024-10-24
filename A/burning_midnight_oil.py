from math import ceil, log

n,k = [int(x) for x in input().split()]

if n <= k:
    print(n)

else:
    start = 1
    end = int(log(n,k)) + 1

    mid = int((start+end)/2)

    while start < end:
        minl = sum([k**i for i in range(mid+1)])

        if n == minl:
            break

        elif minl > n :
            end = mid - 1
        
        else:
            if mid == start:
                break
            start = mid
        
        mid = int((start+end)/2)
    
    p = mid
    start = k**(mid)
    end = (k**(mid+1))-1
    mid = int((start+end)/2)

    while start < end:
        l = sum([int(mid/(k**i)) for i in range(p+1)])

        if n == l:
            break

        elif l > n:
            if mid == end:
                mid -= 1
            end = mid
        
        else:
            start = mid + 1
        
        mid = int((start+end)/2)

    print(mid)