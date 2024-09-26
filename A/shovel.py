y = input().split()
k,r = [int(x) for x in y]
shovels = 1
while True:
    price = (shovels*k)%10
    if  price == r or price == 0:
        print(shovels)
        break
    shovels += 1
