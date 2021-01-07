def selection_sort(nums):
    if len(nums) == 1:
        return nums

    for i in range(len(nums)):
        smallest = i 
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j 
        nums[i], nums[smallest] = nums[smallest], nums[i]

    return nums

s = selection_sort([3,9,8,4,7,9,4,8,4,6,2,2,8,9,7,4,6,5,2,2])

print(s)
