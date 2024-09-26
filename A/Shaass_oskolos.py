n = int(input())
birds = input().split()
birds_on_lines = [int(x) for x in birds]
shots = int(input())
for i in range(shots):
    shot = input().split()
    x,y = [int(pos) for pos in shot]
    x -= 1
    all_birds = birds_on_lines[x]
    left_birds = y - 1
    right_birds = all_birds - left_birds - 1
    birds_on_lines[x] = 0
    if x+1 < n:
        birds_on_lines[x+1] = birds_on_lines[x+1] + right_birds
    if x-1 >= 0:
        birds_on_lines[x-1] = birds_on_lines[x-1] + left_birds

for i in range(n):
    print(birds_on_lines[i])