def tps(i,adj_list,srtd,visited):
    visited[i] = True

    for j in adj_list[i]:
        if not visited[j]:
            tps(j,adj_list,srtd,visited)
    
    srtd.append(i)


n,m = [int(x) for x in input().split()]

while not (n == 0 and m == 0):

    visited = [False for _ in range(n+1)]
    adj_list = [[] for _ in range(n+1)]

    for _ in range(m):
        x,y = [int(z) for z in input().split()]
        adj_list[x].append(y)
    srtd = []

    for i in range(n+1):
        if not visited[i]:
            tps(i,adj_list,srtd,visited)
    
    for k in reversed(srtd[1:]):
        print(k, end=' ')

    print() 



    n,m = [int(x) for x in input().split()]