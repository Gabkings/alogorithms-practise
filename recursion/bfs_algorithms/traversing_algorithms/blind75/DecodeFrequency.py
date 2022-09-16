def frequency(str1):
    res=[0]*26 # Creating an Array for 26 as there are 26 alphabets
    i = len(str1)-1 
    count=1
    while i >= 0:
        j=i
        if str1[i] == ')':
            while str1[j] != '(':
                j=j-1
            count=int(str1[j+1:i])
            i=j
        elif str1[i]=='#':
            j=i-2
            index=int(str1[j:i])
            res[index-1]=1*count
            count=1
            i=j
        elif str1[i] != '(':
            index=int(str1[i])
            res[index-1]=1*count
            count=1
            i=j
        i= i-1
    
    return res

# assert frequency('1226#24#') == [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
print(frequency('1226#24#'))
print(frequency('1(10)226#24#'))

# print(frequency("2110#(2)"))