rolls = input().split()
max_roll = max([int(x) for x in rolls])

chance = 7 - max_roll

if (6/chance) % 1 > 0:
    div = 1/((6/chance) % 1)
    if int(div) > int(6/div):
        print(f'{int(div)}/6')
    else:
        print(f'{int(div)}/{int(6/div)}')
else:
    print(f'1/{int(6/chance)}')

