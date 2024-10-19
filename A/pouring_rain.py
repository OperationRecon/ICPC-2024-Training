from math import pi
d,h,v_down,e = [int(x) for x in input().split()]
v_start = pi*(d/2)**2*h
v_up = pi*(d/2)**2*e
delta_v = v_down-v_up
if delta_v<=0:
    print('NO')
else:
    print('YES')
    print(v_start/delta_v)