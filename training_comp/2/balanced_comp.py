n = int(input())
a = [0]*n
odds = 0
for i in range(n):
    a[i] = int(input())
    if a[i] % 2 != 0:
        odds += 1
odds = odds // 2
for i in range(n):
    if a[i] % 2 == 0:
        a[i] = a[i]//2

    else:
        if odds > 0:
            a[i] = a[i]//2
            odds -= 1
        else:
            a[i] = (a[i]//2)+1
    
    print(a[i])

# AC at 10:46