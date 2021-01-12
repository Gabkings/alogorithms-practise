def recursive_binary_search(nums, element, start, end):
    nums = sorted(nums)
    if start > end:
        return -1 
    
    mid = (start + end) // 2

    if nums[mid] == element:
        return element
    
    elif element < nums[mid]:
        return recursive_binary_search(nums, element, start, mid-1)
    else:
        return recursive_binary_search(nums, element, mid +1, end)

nums = [1,2,4,5,6,7,8,9,10]
l = len(nums)
s = recursive_binary_search([1,2,34,5,6,7], 11,0,l )
print(s)