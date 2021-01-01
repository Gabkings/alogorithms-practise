class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        local_v, global_v = nums[0], nums[0]
        for v in nums[1:]:
            local_v = max(v+local_v, v)
            global_v = max(local_v, global_v)
        return global_v

    def Kadane(arr,n): 
        current_maximum = arr[0]   
        maximum_so_far =arr[0]     
        for i in range(1,n): 
            current_maximum = max(arr[i], current_maximum + arr[i]) 
            maximum_so_far = max(maximum_so_far,current_maximum) 
        return maximum_so_far 
  
arr = [-3, 4, 1, 2, -1, -4, 3] 
print"Maximum sum sum is" , Kadane(arr,len(arr))
