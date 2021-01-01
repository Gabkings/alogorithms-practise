class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        lst3 = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                lst3.append(nums1[i])
        return list(set(lst3)) 

sample = Solution()
p = sample.intersection([1, 2, 2, 1], [2, 2])
print(p)