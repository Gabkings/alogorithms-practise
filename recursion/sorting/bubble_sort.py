def bubble(nums):
    if len(nums) == 1:
        return nums
    
    swapped = True
    while swapped:
        swapped = False 
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
    
    return nums

arr = [7,2,9,7,3,1,5]
s = bubble(arr)
print(s)