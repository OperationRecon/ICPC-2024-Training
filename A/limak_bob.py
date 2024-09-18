wieghts = input().split()
limak,bob = [int(x) for x in wieghts]
years = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    years += 1
print(years)