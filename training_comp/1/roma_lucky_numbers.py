y = input().split()
n,k = [int(x) for x in y]
luckies = 0
numbers = input().split()
for i in numbers:
    if (i.count('7') + i.count('4')) <= k:
        luckies += 1
print(luckies)