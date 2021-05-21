
def solution1(array, targetSum):
    array.sort()
    
    triplets = []
    
    for i in range(len(array)):
        for j in range(i +1, len(array)):
            for k in range(j+1, len(array)):
                result = array[i] + array[j] + array[k]
                if result == targetSum:
                    triplets.append([array[i],array[j],array[k]])
    return triplets

def solution2(array, targetSum):
    array.sort()
    triplets = []
    
    for i in range(len(array) - 2):
        left = i +1 
        right = len(array) - 1
        
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i],array[left], array[right]])
                left += 1
                right -= 1
                
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
                
    return triplets

print(solution1([12,3,1,2,-6,5,-8,6], 0))
print(solution2([12,3,1,2,-6,5,-8,6], 0))