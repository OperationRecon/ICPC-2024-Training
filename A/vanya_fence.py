a = input()
n,h = [int(x) for x in a.split()]
w = 0
heights = input()
heights = [int(x) for x in heights.split()]
for height in heights:
    if height > h:
        w += 2
    else:
        w+=1
print(w)