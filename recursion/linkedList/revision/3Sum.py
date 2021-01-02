class Solution:

    def threeSum(self, nums):
        if not  nums or len(nums) < 3:
            return []

        nums = sorted(nums)

        length = len(nums) - 1

        res = []

        for i in range(length-1):
            if i > 0 and nums[i] == [i-1]:
                continue
            j = i + 1
            k = length

            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if not temp:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j = j +1
                    while j < k and nums[k] == nums[k-1]:
                        k = k -1 
                    k = k -1
                    j = j + 1
                elif temp < 0:
                    j = j + 1
                else:
                    k = k -1 
        return res

sample = Solution()

print(sample.threeSum([-1,0,1,2,-1,-4]))
