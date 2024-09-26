n,k = input().split()
n,k = [int(x) for x in [n,k]]
new_pass = []
for i in range(n):
    new_pass.append(chr(ord('a')+i%k))

print(''.join(new_pass))