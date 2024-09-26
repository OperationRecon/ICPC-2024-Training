time = int(input(),2)
trains = 0

while time > 1:
    time = time / 4
    trains += 1

if time == 0 and trains:
    trains -= 1
    


print(trains)





