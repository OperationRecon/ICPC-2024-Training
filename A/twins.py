n = int(input())
values = [int(x) for x in input().split()]

to_take = 0
to_take_value = 0
total = sum(values)
values = sorted(values)


while to_take <= n and to_take_value <= total:
    total -= values[-1-to_take]
    to_take_value += values[-1-to_take]
    to_take += 1

print(to_take)
