class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_area = 0
        while(l < r):
            length = min(height[l], height[r])
            width = r - l
            area = length * width
            max_area = max(area, max_area)
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return max_area


sln = Solution()

inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]

test = sln.maxArea(inp)

print(test)
