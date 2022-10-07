wordStr = "WeAreTogether"



# function strOut(wordStr) {
#     //split into arr via Capital letters
#     let wordArr = wordStr.split(/(?=[A-Z])/)
#     wordArr[0].toUpperCase()
#     for (let i = 1; i < wordArr.lengh; i++) {
#         wordArr[i].toLowerCase()
#     }
#     let sents = wordArr.join(" ")
#     return sents
# }
import re
def strOut(wordStr):
    # wordArr = wordStr.split('/(?=[A-Z])/')
    wordArr = re.findall('[A-Z][^A-Z]*', wordStr)
    # str1 = "gabriel.gitonga@gmail.com"
    # wordArr = str1.split("@")
    # wordArr1 = wordArr[0].split(".")

    # wordArr2 = " ".join(wordArr1).title()

    print(wordArr)

    return " ".join(wordArr).capitalize()

print(strOut(wordStr))

def strToLatin(str):
    sentence = input("Please enter a word \n")
    first = sentence[0]
    length = len(sentence)
    rest = sentence[1:length]
    if first =="a" and first == "e" and first == "i" and first == "o" and first == "u":
        return rest + first + "ay"
    else:
        return sentence + "way"

# def generateParenthesis(n):
#     stack = []
#     res = []

#     def backtrack(openN, closedN):
#         if openN == closedN == n:
#             return res.append("".join(stack))
#             return 

#         if openN < n:
#             stack.append("(")
#             backtrack(openN + 1, closedN)
#             stack.pop()
        
#         if closedN < openN:
#             stack.append(")")
#             backtrack(openN, closedN + 1)
#             stack.pop()

#     backtrack(0, 0)

#     return res

def reverseSentense(str):

    str = str.strip()

    str = str.split(" ")

    str = [i for i in str if i != ""]

    i = 0
    j = len(str)-1

    while i < j:
        str[i], str[j] = str[j], str[i]

        j -= 1
        i += 1
    return " ".join(str)


# print(reverseSentense("iLoveYou"))

def reverseString(str1):
    s = ""
    for i in str1:
        s = i + s
    return s

# print(reverseString("iLoveYou"))


def findTotalPower(power):
    total = 0 
    for l in range(len(power)):
        for r in range(l, len(power)):
            pwr = min(power[l:r+1]) * sum(power[l:r+1])
            total += pwr 

    return total % (10**9 + 7)



power = [2,3,2,1]

print(findTotalPower(power))


def swaps(arr, n):
    res = 0 
    max_i, min_i = max(arr), min(arr)

    if min_i == max_i:
        return 0 
    
    index_max, index_min = -1,-1
    for i in range(n):
        if arr[i] == max_i and index_max == -1:
            index_max = i 
        
        if arr[i] == min_i:
            index_min = i 

    res += index_min 

    res += (n-1-index_max)

    if index_min > index_max:
        res -= 1 

    return res 