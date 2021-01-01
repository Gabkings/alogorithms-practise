class Solution:
    """
    @param arrs: an array of arrays
    @return: return the max distance among arrays
    """
    def maxDiff(self, arrs):
        # write your code here
        result, min_val, max_val = 0, arrs[0][0], arrs[0][-1]
        
        for i in range(1, len(arrs)):
            result =max(result, max(max_val - arrs[i][0], arrs[i][-1] - min_val))
            min_val = min(min_val, arrs[i][0])
            max_val = max(max_val, arrs[i][-1])
        return result

sample = Solution()

print(sample.maxDiff([[1,2,3], [4,5], [1,2,3]]))