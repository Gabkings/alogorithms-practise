# def WordSplit(strArr):
#     first_element = strArr[0]
#     second_element = strArr[1].split(',')
#     p = []
#     p1 = []
#     for i in range(len(second_element)):
#         r = first_element.split(second_element[i])
#         if len(r) == 2:
#             k = r[0]+r[1]
#             p.append(k)
#     for j in range(len(p)):
#         if second_element.count(p[j]) != 0:
#             p1.append(p[j])
#     l = []
#     if p1 == []:
#         l = 'Not possible'
#     else:
#         for i in range(len(p1)):
#             for j in range(len(p1)):
#                 n = p1[i]+p1[j]
#                 if n == first_element:
#                     l.append(p1[i])
#                     l.append(p1[j])
#                     l = ','.join(l)

#     # code goes here
#     return l


# # keep this function call here
# #
# inpArr = ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]
# print(WordSplit(inpArr))


from collections import Counter


def searchingChallenge(strArr):
    result = Counter()
    for s in strArr:
        item, count = s.split(":")
        result[item] += int(count)

    return result


strArr = ["B:-1", "C:3", "A:1", "B:3", "C:2", "A:5"]

print(searchingChallenge(strArr))
