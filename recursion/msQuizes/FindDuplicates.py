myList = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]

occurrences = []

for item in myList:
    count = 0 
    for x in myList:
        if x == item:
            count += 1
    occurrences.append(count)

dublicates = set()
print(occurrences)
index = 0
while index < len(myList):
    if occurrences[index] == 1:
        dublicates.add(myList[index])
    index += 1

print(dublicates)


def removeDublicates(nums):
    if len(nums) == 0:
        return 0

    length = 0
    index = 1
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != prev:
            length += 1
            prev = nums[i]
            nums[index] = nums[i]
            index += 1
    
    return length

# print(removeDublicates())

def bestTimeTosell(prices):
    maxProfic = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxProfic += prices[i] - prices[i-1]

    return maxProfic

def rotateArr(nums):
    length = len(nums)
    a = [0] * length
    for i in range(length):
        a[(i +k) % length] = nums[i]
    nums[:] = a 
    return nums

def plusOne(digits):
    if digits[-1] < 9:
        digits[-1] = digits[-1] +1
    else:
        if len(digits) == 1:
            digits = [1,0]
        else:
            digits = self.plusOne(digits[:-1]) + [0]
    
    return digits

def twoSum(nums, target: int):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]


# print(twoSum([2,3,7,15],9))