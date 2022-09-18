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

print(reverseString("iLoveYou"))