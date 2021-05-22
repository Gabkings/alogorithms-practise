# o(nlong n) time | o(n) space
def solution1(array):
    newArr = []
    
    for i in array:
        newArr.append(i*i)
    newArr.sort()
    
    return newArr

# o(n) time | o(n) space
def solution2(array):
    
    newArr = [0 for _ in array]
    
    smallestIndex = 0
    largestIndex = len(array) - 1
    
    for idx in reversed(range(len(array))):
        smallestValue = array[smallestIndex]
        largestValue = array[largestIndex]
        if abs(smallestValue) > abs(largestValue):
            newArr[idx] = smallestValue * smallestValue
            smallestIndex += 1
        else:
            newArr[idx] = largestValue * largestValue
            largestIndex -= 1
            
    return newArr


array = [1,2,3,5,6,8,9]

print(solution1(array))
print(solution2(array))