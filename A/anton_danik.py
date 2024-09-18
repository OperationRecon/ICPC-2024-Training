n = input()
dubs = input()
anton_dubs =0
danik_dubs =0
for dub in dubs:
    if dub == 'A':
        anton_dubs += 1
    else:
        danik_dubs += 1

if anton_dubs > danik_dubs:
    print("Anton")
elif anton_dubs == danik_dubs:
    print('Friendship')
else:
    print('Danik')