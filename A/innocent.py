t = int(input())
for i in range(t):
    frq = {x:[] for x in range(-10**9,10**9+1)}
    n, q = [int(x) for x in input().split()]
    ans = [int(x) for x in input().split()]
    for j in range(1,n+1):

        frq[ans[j]] = j
    
    for k in range(q):
        s = input().split()
        if s[0] == '1':
            c = 0
            for x in frq[3]:
                if x >= s[1] and s <= s[2]:
                    c+=1
            print(c)
        else:
            tmp = ans[s[1]]
            ans[s[1]] = s[2]
            frq[tmp].remove(s[1])
            frq[s[2]].append(s[1])
