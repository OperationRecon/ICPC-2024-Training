stones = input()
commands = input()
command = 0
stone = 0
while command < len(commands):
    if commands[command] == stones[stone]:
        stone += 1
    command += 1

print(stone+1)