n = int(input())
bags = input().split()
bags = [int(x) for x in bags]
total = sum(bags)
steals = 0
for bag in bags:
    if (total - bag) % 2 == 0:
        steals += 1

print(steals)