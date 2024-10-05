global k, visited
global new_graph
new_graph = {}

def dfs(node, graph, visit = 0):
    if len(graph[node]) > 1:
        for i in ((graph[node])):
            if i != visit:
                return 1 + dfs(i,graph,node,)
    else:
        return 1            
    
def bfs(node,parent,graph):
    global visited, new_graph
    for x in graph[node]:
        new_graph[node] = [] if node not in new_graph else new_graph[node]

        if visited < k:
            if x != parent:
                visited += 1
                new_graph[node].append(x)
                new_graph[x] = []
        else:
            return
        
    for z in graph[node]:
        bfs(z,node,graph)



n,k = [int(x) for x in input().split()]

graph = {x:[] for x in range(1,n+1)}
n_nodes = [0]*n

for i in range(n-1):
    x,y = [int(z) for z in input().split()]

    graph[x].append(y)
    n_nodes[x-1] += 1
    graph[y].append(x)
    n_nodes[y-1] += 1

start = 0

for i in range(n):
    if n_nodes[start] < n_nodes[i]:
        start = i

visited = 1
start += 1
queue = graph[start]

bfs(start,-1,graph)
costs = [0]*len(new_graph[start])
for i in range(len(new_graph[start])):
    costs[i] = dfs(new_graph[start][i],new_graph,)

costs.append(0)
costs.sort(reverse=True)
print(costs[0]+costs[1]+1)


    




    




