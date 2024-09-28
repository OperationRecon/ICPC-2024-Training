import math
while True:
    try:
        y = input().split()
        step, mod = [x for x in y]
        print(' '*(10-(len(step)))+step+' '*(10-(len(mod)))+mod+' '*4,end='')
        if math.gcd(int(step),int(mod)) == 1:
            print('Good Choice')
        else:
            print('Bad Choice')
        print()

    except:
        break

    