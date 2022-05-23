
import collections
class Solution:
    '''
    Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle
    '''
    def tilingRectangle(self, n, m):

        if m > n:
            m,n = n, m

        target = [n]*m

        # a state is the height array, and the number squares used

        q = collections.deque([([0]*m, 0)])

        while q:
            height, moves = q.popleft()

            if height == target:
                return moves
            
            # try to fill the sqare in the minmum height first
            minHeight = float("inf")
            idx = None
            for i, h in enumerate(height):
                if h < minHeight:
                    minHeight = h
                    idx = i

            # find the largest sqare we can use at minmum height

            rIdx = idx + 1

            while rIdx < m and height[rIdx] == minHeight:
                rIdx += 1
            maxHeightToBeAdded = min(rIdx - idx, n - minHeight)

            for i in range(maxHeightToBeAdded,0, -1):
                newHeight = height[:]
                for j in range(i):
                    newHeight[idx + j] += i
                q.append((newHeight, moves+1))

test = Solution()

print(test.tilingRectangle(2, 3))