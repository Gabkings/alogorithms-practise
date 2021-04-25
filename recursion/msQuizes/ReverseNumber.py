# number = int(input("Enter a number to reverse"))
# reverse_num = 0 
# while number > 0:
#     remainder = number % 10
#     reverse_num = (reverse_num * 10) + remainder
#     number = number // 10

# print(reverse_num)

# def solution(N):
#     enable_print = N % 10
#     while N > 0:
#         if enable_print == 0:
#             enable_print = 1
#         elif enable_print == 1:
#             print(N % 10, end=" ")
#         N = N // 10

# solution(1)


# import re

# def pathholes(s):
#     res = [iters.group(0) for iters in re.finditer(r"(\D)\1*", s)]
#     return res

# print(pathholes("...xxx..x...xxx"))


def solution(s, b):
    lst = s.split('.')
    print(lst)
    potholes = ' '.join(lst).split()
    print(potholes)
    potholes.sort(key=len, reverse=True)
    resp = 0
    for i in potholes:
        if b <= 0:
            break
        if len(i) + 1 <= b:
            resp += len(i)
            b -= len(i) + 1
        else:
            rem = b - 1
            resp += rem
            b -= b


    return resp
s = "..xxxxx"
b = 4
print(solution(s, b))