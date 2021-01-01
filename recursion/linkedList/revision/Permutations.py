class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        length = len(nums)
        if length == 0:
            return [[]]
        if length == 1:
            return [nums]
        res = []
        for i in range(length):
            for j in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        return res

sample = Solution()

print(sample.permute([1,2,4,3]))