n = int(input())
ok = True
piars = {x:7-x for x in range(1,7)}
top = int(input())
s1,s2 = [int(x) for x in input().split()]

for i in range(n-1):
    s3,s4 = [int(x) for x in input().split()]
    
    if not ok:
        continue

    invalid = (s1,s2,piars[s1],piars[s2])

    for s in (s3,s4):
        if s in invalid:
            if i == 0:
                if (top not in (s3,s4,piars[s3],piars[s4])) and (piars[top] not in (s3,s4,piars[s3],piars[s4])):
                    continue
            ok = False
            break

    s1,s2 = s3,s4

if ok:
    print('YES')
else:
    print('NO')