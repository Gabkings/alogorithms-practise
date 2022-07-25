class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(1, n):
                length = min(height[i], height[j])
                width = j-i
                area = length * width
                max_area = max(max_area, area)
        
        return max_area
    
    def maxArea2(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while (l < r):
            legth = min(height[l], height[r])
            width = r - l
            area = legth * width 
            max_area = max(area, max_area)

            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        
        return max_area

ob = Solution()
heights = [1,8,6,2,5,7]

print(ob.maxArea2(heights))