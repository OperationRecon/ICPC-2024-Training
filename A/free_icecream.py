nx = input().split()
n,x = [int(x) for x in nx]
icecream = x
distressed = 0
for i in range(n):
    queued = input().split()
    if queued[0] == '+':
        icecream += int(queued[1])
    else:
        to_take = int(queued[1])
        if to_take > icecream:
            distressed += 1
        else:
            icecream -= to_take
print(icecream,distressed)
