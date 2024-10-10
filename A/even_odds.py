from math import ceil
n,k = [int(x) for x in input().split()]
if k > ceil(n/2):
    print(2*(k-ceil(n/2)))
else:
    print(2*k-1)