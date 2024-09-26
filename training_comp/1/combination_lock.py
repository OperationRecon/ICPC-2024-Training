n = int(input())
c = input()
t = input()
steps = 0
for i in range(n):
    c_digit = int(c[i])
    t_digit = int(t[i])
    diff = abs(c_digit-t_digit)
    steps += min(diff,10-diff)
print(steps)


# 12:18