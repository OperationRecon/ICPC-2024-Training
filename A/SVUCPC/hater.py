nyuyu= int(input())
for loloko in range(nyuyu):
    n,k = [int(x) for x in input().split()]
    numbers = sorted([int(x) for x in input().split()])
    dic = {}
    for i in numbers:
        dic[i] = False
    print(numbers)
    differnces = []
    for i in range(n):
        if i == 0:
            if len(numbers) >= 2 and numbers[i] == numbers[1]:
                continue
            else:
                differnces.append(numbers[i])
                dic[numbers[i]] = True

        elif i == n-1 and numbers[i-1]!=numbers[i]:
            differnces.append(numbers[i])
            dic[numbers[i]] = True

        elif numbers[i-1]!=numbers[i] and numbers[i+1]!=numbers[i]:
            differnces.append(numbers[i])
            dic[numbers[i]] = True


    
