
def frequency(s):
    res = [0] * 26 

    n  = len(s),
    i =  n-1
    while i >= 0:
        cnt, num = 1, 0
        if s[i] == ')':
            i, ts = 1, 0
            while s[i] != '(':
                cnt = int(s[i]) * (10**ts)
                ts += 1
                i-= 1
            i -= 1
        if s[i] == '#':
            i -= 2 
            num = int(s[i]) * 10 + int(s[i + 1])
        if num == 0:
            num = int(s[i])
        res[num - 1] += cnt 

        i -= 1

    return "".join(map(str, res))

print(frequency("2110#(2)"))