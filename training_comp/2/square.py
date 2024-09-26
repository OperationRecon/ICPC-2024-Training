import math
y = input().split()
n,m,a = [int(x) for x in y]
hori = math.ceil(n/a)
vert = math.ceil(m/a)

print(hori*vert)