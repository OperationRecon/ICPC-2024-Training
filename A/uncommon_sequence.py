a = input()
b = input()
found = False

if a == b:
    print(-1)
    found = True

if len(b) < len(a):
    a,b = b,a

for i in range(len(b)):
    for j in range(i+1):
        if found:
            break

        subs_b = b[j:j+len(b)-i]
        subs_a = ''.join([x for x in a if x in subs_b])

        if subs_a != subs_b or subs_a == '':
            print(max(len(subs_a),len(subs_b)))
            found = True
            break
    if found:
        break



