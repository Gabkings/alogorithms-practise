class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            # when the element is not i
            while nums[1] != i + 1:
                # no need to swap if the element is out of the range
                if(nums[i] < 0 or nums[i] >= n):
                    break
                # handle dublicate elements
                if(nums[i] == nums[nums[i] - 1]):
                    break
                # swap elements 
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp

        for i in range(n):
            if(nums[i] != i + 1):
                return i + 1

        return n + 1


nums = [1,2,0]

sln = Solution()
print(sln.firstMissingPositive(nums))
