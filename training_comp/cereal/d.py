n,m = map(int,input().split())

if m%n == 0:
    for _ in range(m//n):
        print("1"*n)
    for _ in range(n-(m//n)):
        print("0"*n)
else:
    k = m//n
    l = k
    for _ in range(k):
        print("1"*n)
    if m%n != 0:
        print("1"*(m%n)+"0"*(n-(m%n)))
        l +=1
    for _ in range(n-l):
        print("0"*n)
    