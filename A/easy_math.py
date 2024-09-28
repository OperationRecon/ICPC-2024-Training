n = int(input())
for i in range(n):
    y = input().split()
    n,m,a,d = [int(x) for x in y]
    oke = m - n + 1

    notoke = sum([(1/(a+i*d))for i in range(5)])

    for i in range(5):
        for j in range(i,5):
            if i == j:
                continue
            notoke -= (1/(a+i*d))*(1/(a+j*d))

    for i in range(5):
        for j in range(i,5):
            if i == j:
                continue
            for k in range(j,5):
                if k == j:
                    continue
                notoke += (1/(a+i*d))*(1/(a+j*d))*(1/(a+k*d))

    for i in range(5):
        for j in range(i,5):
            if i == j:
                continue
            for k in range(j,5):
                if k == j:
                    continue
                for l in range(k,5):
                    if l == k:
                        continue
                    notoke -= (1/(a+i*d))*(1/(a+j*d))*(1/(a+k*d))*(1/(a+l*d))

    for i in range(5):
        for j in range(i,5):
            if i == j:
                continue
            for k in range(j,5):
                if k == j:
                    continue
                for l in range(k,5):
                    if l == k:
                        continue
                    for o in range(l,5):
                        if l == o:
                            continue
                        notoke += (1/(a+i*d))*(1/(a+j*d))*(1/(a+k*d))*(1/(a+l*d))*(1/(a+o*d))

    
    print(oke//notoke)