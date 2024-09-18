n = int(input())
to_solve = 0
for i in range(n):
    certainty = input()
    if certainty.count('1') >= 2:
        to_solve += 1
print(to_solve)