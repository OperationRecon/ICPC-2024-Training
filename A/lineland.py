n = int(input())
pos = [int(x) for x in input().split()]
for i in range(n):
    if i == 0:
        print(pos[1]-pos[i],pos[-1]-pos[i])
    elif i == n-1:
        print(pos[i]-pos[-2],pos[i]-pos[0])

    else:
        print(min(pos[i]-pos[i-1],pos[i+1]-pos[i]),max(pos[i]-pos[0],pos[-1]-pos[i]))