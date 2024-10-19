n = int(input())
diag = None
other = None
good = True
for i in range(n):
    ln = input()
    diag = ln[0] if not diag else diag
    other = ln[1] if not other else other
    if ln[i] != diag or ln[-1-i] != diag or diag == other:
        good = False
        break
    for j in range(n):
        if j in (i,n-1-i):
            continue
        if ln[j] != other:
            good = False
            break

if good:
    print('YES')
else:
    print('NO')
