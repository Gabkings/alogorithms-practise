
def find_element(nums, target):
    length = len(nums)
    st = 0
    end = length - 1

    while st < end:
        mid = (st + end) // 2
        if nums[mid][1] > target:
            end = mid + 1
        else:
            st = mid 
    return nums[st]


def optimalUtilization(a,b, target):
    a.sort(key = lambda x:x[1])
    b.sort(key = lambda x:x[1])

    len1 = len(a)
    len2 = len(b)

    curval = 0 
    res = []

    for idx1, num1 in a:
        idx2, num2 = find_element(b, target - num1)
        if num1 + num2 <= target:
            curval = num1 + num2 
            res = [[idx1, idx2]]
        elif curval == num1 + num2:
            res.append([idx1, idx2])

    return res 

a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
print(optimalUtilization(a, b, target))