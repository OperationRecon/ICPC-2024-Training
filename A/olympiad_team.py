students = int(input())
mathers = []
physers = []
progers = []
groups = []
specials = input().split()
for i in range(students):
    if specials[i] == '1':
        progers.append(i+1)
    elif specials[i] == '2':
        mathers.append(i+1)
    else:
        physers.append(i+1)
    
    if len(mathers) > 0 and len(progers) > 0 and len(physers) > 0:
        groups.append([progers.pop(0),mathers.pop(0),physers.pop(0)])

print(len(groups))

for team in groups:
    print(team[0],team[1],team[2])
    