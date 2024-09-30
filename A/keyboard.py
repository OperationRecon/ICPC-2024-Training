l_or_r = input()
diff = 1 if l_or_r == 'R' else -1
message = input()
out = []
toprow = 'qwertyuiop'
midrow = 'asdfghjkl;'
bottom_row = 'zxcvbnm,./'
out = []

for i in range(len(message)):
    if message[i] in toprow:
        out.append(toprow[toprow.index(message[i])-diff])

    elif message[i] in midrow:
        out.append(midrow[midrow.index(message[i])-diff])

    else:
        out.append(bottom_row[bottom_row.index(message[i])-diff])

print(''.join(out))
