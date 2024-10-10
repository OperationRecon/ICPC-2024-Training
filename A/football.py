g = int(input())
scoresheet = {}
for i in range(g):
    team = input()
    if team not in scoresheet:
        scoresheet[team] = 0
    else:
        scoresheet[team] += 1
winner = max(scoresheet.values())
for i in scoresheet.keys():
    if scoresheet[i] == winner:
        print(i)