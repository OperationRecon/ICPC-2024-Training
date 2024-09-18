n = int(input())
ones_zeroes = input()
i = 0

while i < len(ones_zeroes)-1:
    if ones_zeroes[i:i+1].is '010':
        ones_zeroes = ones_zeroes[:i-1]+ones_zeroes[i+2:]
        i -= 1
        continue
    i += 1
print(len(ones_zeroes))