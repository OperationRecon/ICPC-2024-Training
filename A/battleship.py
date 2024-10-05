def check_ship(i,j,visited,grid,N,destroyed = True, direction = None):
    visited[i][j] = True
    if grid[i][j] == 'x':
        destroyed = False
    
    if not direction:
        mods = ((0,1),(1,0),(0,-1),(-1,0))
        for d in mods:
            if i+d[0] >= N or i+d[0] < 0 or j+d[1] >= N or j+d[1] < 0:
                continue

            elif not visited[i+d[0]][j+d[1]] and grid[i+d[0]][j+d[1]] != '.':
                destroyed = check_ship(i+d[0],j+d[1],visited,grid,N,destroyed,d)
    
    elif i+direction[0] < N and i+direction[0] >= 0 and j+direction[1] < N and j+direction[1] >= 0:
        if not visited[i+direction[0]][j+direction[1]] and grid[i+direction[0]][j+direction[1]] != '.':
            destroyed = check_ship(i+direction[0],j+direction[1],visited,grid,N,destroyed,direction)
    
    return destroyed

T = int(input())
for case in range(1,T+1):
    N = int(input())
    grid = [[x for x in input()] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    ships = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] != '.':
                destroyed = check_ship(i,j,visited,grid,N)
                if not destroyed:
                    ships += 1
    
    print(f'Case {case}: {ships}')