import math
bulbs = []
bulb = int(input())

while bulb != 0:
    if math.sqrt(bulb)%1 == 0:
        print('yes')
    else:
        print('no')
    bulb = int(input())

