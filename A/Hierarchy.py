# def check_hierarchy(i,j,emps):
#     # if j is a superior to i
#     if j in emps[i]['subords']:
#         return False
    
#     elif i in emps[i]['subords'] or not emps[j]['boss']:
#         return True
    
#     else:
#         return check_hierarchy(i,emps[j]["boss"],emps)

# n,k = [int(x) for x in input().split()]
# emps = {x:{'boss':0,} for x in range(1,n+1)}

# for i in range(1,k+1):
#     l = [int(x) for x in input().split()]
#     w = l[0]
#     for j in range(1,w+1):
#         if 'subords' not in emps[i]:
#             emps[i]['subords'] = [l[j]]
        
#         else:
#             emps[i]['subords'].append(l[j])

# for i in range(1,k+1):

#     for j in emps[i]['subords']:

#         if not emps[j]['boss']:
#             emps[j]['boss'] = i
        
#         else:
#             superior = check_hierarchy(i,emps[j]['boss'],emps)
            
#             if not superior:
#                 if emps[emps[j]['boss']]['boss']:
#                     emps[i]['boss'] = emps[emps[j]['boss']]['boss']
#                 emps[emps[j]['boss']]['boss'] = i
            
#             else:
#                 emps[i]['boss'] = emps[j]['boss']
#                 emps[j]['boss'] = i
#         if emps[i]['boss'] == i:
#             emps[i]['boss'] = 0
# for j in range(k+1,n+1):
#     if not emps[j]["boss"]:
#         emps[j]["boss"] = k

# for i in emps.values():
#     print(i['boss'])

def tps(i,adj_list,srted,visited):
    visited[i] = True
    if i < len(adj_list):
        for  j in adj_list[i]:
            if not visited[j]:
                tps(j,adj_list,srted,visited)
    
    srted.append(i)


n, k = [int(x) for x in input().split()]
visited = [False for _ in range(n)]
adj_list = [[int(x) - 1 for x in input().split()[1:]] for _ in range(k)]
srted = []

for i in range(n):
    if not visited[i]:
        tps(i,adj_list,srted,visited)

boss = [0 for _ in range(n)]
for i in range(n-1):
    boss[srted[-i-2]] = srted[-i-1]+1

for i in range(n):
    print(boss[i])
