x = input()
n,m = [int(y) for y in x.split()]
body = '#'*m
space = '.'*(m-1)
left = True
for i in range(n):
    if i % 2 == 0:
        print(body)
    else:
        if left:
            print(space+'#')
        else:
            print('#'+space)
        left = not left