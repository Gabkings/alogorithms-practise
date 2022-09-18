'''
Given a String find the minimum number of reduce operations required to convert a given string into a palindrome. 
In a reduce operation, we can change character to a immediate lower value.
For example b can be covered to a.
'''

def coutReduce(str):
    n = len(str)
    res = 0
    for i in range(0, int(n/2)):
        res += abs(int(ord(str[i])) - int(ord(str[n - i - 1])))
    return res

print(coutReduce("abcd"))