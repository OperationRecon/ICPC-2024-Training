import math
tests = int(input())
for i in range(tests):
    p = int(input())
    contributions = [int(x) for x in input().split() if x != '0']
    contributions.sort(reverse=True)
    max_goals = sum(contributions)
    min_goals = 0
    i = 0
    j = 1

    print(max(math.ceil(max_goals/2),max(contributions)),max_goals)