n = int(input())
recievers = {str(x):0 for x in range(1,n+1)}
givers = input().split()
for i in range(len(givers)):
    recievers[givers[i]] = i+1

for i in recievers.values():
    print(i,end=' ')

print() 

