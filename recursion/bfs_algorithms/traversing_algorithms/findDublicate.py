class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = f = nums[0]
        while True:
            s, f = nums[s], nums[nums[f]]
            if s == f:
                break
        s = nums[0]
        while s != f:
            s, f = nums[s], nums[f]
        return s


sln = Solution()
nums = [1, 3, 4, 2, 2]
print(sln.findDuplicate(nums))
