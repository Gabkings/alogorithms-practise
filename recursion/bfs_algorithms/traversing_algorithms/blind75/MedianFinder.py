
import heapq
class Solution:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num):
        heapq.heappush(small, -1 * num)
        # make sure that evry num small <= evry num in large 
        if(small and large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size 
        if(len(small) > len(large) + 1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(large, val)

        if(len(large) > len(small) + 1):
            val = heapq.heappop(self.large)
            heapq.heappush(small,-1 * val)
            
    def findMedian(self):
        if len(small) > len(large):
            return self.small[0]
        if len(large) > len(small):
            return self.large[0]
        return (self.small[0] + self.large[0]) / 2


class MedianFinder(object):
    
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num):
        heappush(self.lo, -num)

		# we only need to balance here if there are too many numbers in the lows,
		# or if the newly added number is larger than the smallest in the highs
        if len(self.lo) - len(self.hi) > 1 or (self.hi and -self.lo[0] > self.hi[0]):
            largest = heappop(self.lo)
            heappush(self.hi, -largest)
            
		# we need to shrink the highs if they grew from the previous step
        if len(self.hi) > len(self.lo):
            smallest = heappop(self.hi)
            heappush(self.lo, -smallest)
        
    def findMedian(self):
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2

        return -self.lo[0]