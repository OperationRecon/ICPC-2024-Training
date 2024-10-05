t = int(input())
for p in range(t):
    n = int(input())
    s = input()
    digits = [int(x) for x in s]
    big = 0
    small = 0
    for i in range(n):
        if digits[big] >= digits[i]:
            big = i
    for i in range(n):
        if digits[small] >= digits[i] and digits[small] < digits[big]:
            small = i
        
    no_ops = 0

    if digits[small] == digits[big]:
        no_ops = 0
    
    elif min(small,big) == 0 and max(small,big) == n-1:
        if small < big:
            no_ops = 0
        else:
            no_ops = 1
            if big == 0:
                big = small
            digits[0],digits[small] = digits[small],digits[0]
            

    
    else:
        if digits[small] != digits[0]:
            no_ops += 1
            if big == 0:
                big = small
            digits[0],digits[small] = digits[small],digits[0]

        if digits[big] != digits[-1]:
            no_ops += 1
            digits[-1],digits[big] = digits[big],digits[-1]
    

    
    total = 0
    for i in range(n-1):
        total += digits[i]*10+digits[i+1]

    print(digits)
    print(no_ops,total)