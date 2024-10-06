def dfs(player,adj_list,visited,):
    last_player = player
    visited[player] = True
    chain = 1
    for i in adj_list[player]:
        if not visited[i]:
            ln,last_player = dfs(i,adj_list,visited)
            chain += ln

    return  chain, last_player           

n,m = [int(x) for x in input().split()]
adj_list = {x+1:[] for x in range(n)}
for i in range(m):
    x,y = [int(z) for z in input().split()]
    adj_list[x].append(y)
    adj_list[y].append(x)


free = 0
benched = 0
visited = [False for _ in range(n+1)]
for player, enemies in adj_list.items():

    if visited[player]:
        continue

    chain_length,last_player = dfs(player,adj_list,visited)

    if len(adj_list[last_player]) >= 2:
        if chain_length % 2 != 0:
            benched += 1
    
    elif chain_length % 2 != 0:
        free += 1

if free % 2 != 0:
    benched += 1

print(benched)    

