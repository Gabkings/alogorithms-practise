def func(string):
    Tleft = [0]*len(string)
    Hright = [0]*len(string)

    result = len(string)
    # iterate from 1 since Tleft[0] is always 0

    for i in range(1, len(string)):
        if string[i-1] == 'T':
            Tleft[i] = Tleft[i -1] + 1
        else:
            Tleft[i] = Tleft[i - 1]
    
    # iterate from 2 to last element as Hright[lastIndex] is always 0

    for i in range(len(string)-2, -1,-1):
        if string[i+1] == 'H':
            Hright[i] = Hright[i + 1] + 1
        else:
            Hright[i] = Hright[i + 1]
    
    for i in range(len(string)):
        result = min(result, Tleft[i] + Hright[i])
    
    if result != 0:
        return result
    return 1

string = 'THHHTH'

print(func(string))