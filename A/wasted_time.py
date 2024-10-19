from math import sqrt
n, k = [int(x) for x in input().split()]
x1, y1 = [int(x) for x in input().split()]
dist = 0
for i in range(n-1):
    x2, y2 = [int(x) for x in input().split()]
    dist += sqrt((x2-x1)**2+(y2-y1)**2)
    x1,y1 = x2,y2

secs = dist/50
print(k*secs)