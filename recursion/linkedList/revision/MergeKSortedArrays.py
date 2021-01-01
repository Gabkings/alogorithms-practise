from heapq import merge
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        length = len(arrays)
        l = arrays[0]
        for i in range(length-1):
            l = list(merge(l, arrays[i+1]))
        return l
    


sample = Solution()
arr = sample.mergekSortedArrays([[1,2,3],[4,5,6],[7,8,9]])
print(arr)