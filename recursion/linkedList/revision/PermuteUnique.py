class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0: return [[]]
        if length == 1: return [nums]
        nums.sort()
        res = []
        previousNum = None
        for i in range(length):
            
            if nums[i] == previousNum: continue
            previousNum = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res