def dfs (i,j,visited,img,dim):
    ii_mod = [-1,0,1]
    jj_mod = [-1,0,1]
    visited[i][j] = True
    for ii in ii_mod:
        if i + ii >= dim or i + ii < 0:
            continue
        else:
            for jj in jj_mod:
                if j + jj >= dim or j + jj < 0:
                    continue
                elif not visited[i+ii][j+jj] and img[i+ii][j+jj] == '1':
                    dfs(i+ii,j+jj,visited,img,dim)

n = 1
while True:
    try:
        dim = int(input())
        img = [[x for x in input()] for _ in range(dim)]
        visited = [[False for _ in range(dim)] for _ in range(dim)]
        eagles = 0
        for i in range(dim):
            for j in range(dim):
                if not visited[i][j] and img[i][j] == '1':
                    dfs(i,j,visited,img,dim)
                    eagles += 1
        print(f'Image number {n} contains {eagles} war eagles.')
        n += 1

    except EOFError:
        break
