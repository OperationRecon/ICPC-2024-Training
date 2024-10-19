w = int(input())
for _ in range(w):
    n,m = map(int,input().split())
    str = ""
    for _ in range(n):
        str+= input()
    flip1 = 0
    flip2 = 0
    if m % 2 == 1:
        for i,j in enumerate(str):
            if i % 2 ==0:
                if j == "1":
                    flip1 +=1
                else:
                    flip2 +=1
            else:
                if j == "0":
                    flip1 +=1
                else:
                    flip2 +=1
    else:
        for i,j in enumerate(str):
            if (i//m) % 2 ==0:
                if i % 2 ==0:
                    if j == "1":
                        flip1 +=1
                    else:
                        flip2 +=1
                else:
                    if j == "0":
                        flip1 +=1
                    else:
                        flip2 +=1
            else:
                if i % 2 ==0:
                    if j == "1":
                        flip2 +=1
                    else:
                        flip1 +=1
                else:
                    if j == "0":
                        flip2 +=1
                    else:
                        flip1 +=1

    if flip1 < flip2:
        print(flip1)
    else:
        print(flip2)