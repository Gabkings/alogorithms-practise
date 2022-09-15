def simpleCipher(encryPted, k):
    k %= 26

    result = ""
    for char in encryPted:
        value = ord(char) - ord('A') - k 
        if value < 0:
            value += 26 

        value += ord('A')
        result += chr(value)

    return result

encryPted = 'VTAOG'
k = 2

print(simpleCipher(encryPted, k))