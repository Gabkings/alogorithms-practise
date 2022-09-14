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
# import re
# def strOut(wordStr):
#     # wordArr = wordStr.split('/(?=[A-Z])/')
#     wordArr = re.findall('[A-Z][^A-Z]*', wordStr)

#     return " ".join(wordArr).capitalize()

# print(strOut(wordStr))

sentence = input("Please enter a word \n")
first = sentence[0]
length = len(sentence)
rest = sentence[1:length]
if first =="a" and first == "e" and first == "i" and first == "o" and first == "u":
    nw = rest + first + "ay"
else:
    sentence + "way"

print(nw.lower())