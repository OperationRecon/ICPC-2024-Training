def get_weight(current,level):
    if level <= 1:
        return 1
    
    if current == level:
        l_parent = 0
    else:
        l_parent = get_weight(current+1,level-1)
    
    if current == -level:
        r_parent = 0
    else:
        r_parent = get_weight(current-1,level-1)
    
    return r_parent+l_parent

actual = input()
recived = input()
actual_pos_offset = actual.count('+') - actual.count('-')
recived_pos_offset = recived.count('+') -recived.count('-')
unknowns = recived.count('?')
diff = abs(actual_pos_offset - recived_pos_offset)
if diff > unknowns:
    print(0)
else:
    if diff % 2 != unknowns % 2:
        print(0)
    else:
        print((get_weight(diff,unknowns))/(2**unknowns))


    
