class Solution:
    '''
    Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.
    '''

    def closedIsland(self, grid):
        R = len(grid)
        C = len(grid[0])

        res = 0

        #DFS loop

        def visit(r,c):
            if 0 <= r < R and 0 <= c < C and grid[r][c] == 0:
                grid[r][c] = -1

                for nr, nc in [(r+1, c), (r-1,c), (r,c+1), (r,c-1)]:
                    visit(nr, nc)

        # mark off the islands on first and last rows
        for r in [0, R-1]:
            for c in range(C):
                if grid[r][c] == 0:
                    visit(r, c)

        # mark off the islands on first and last columns

        for c in [0, C-1]:
            for r in range(R):
                if grid[r][c] == 0:
                    visit(r, c)

        # count the connected components 

        for r in range(1, R-1):
            for c in range(1, C-1):
                if grid[r][c] == 0:
                    res += 1
                    visit(r, c)

        return res


test = Solution()


grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]

print(test.closedIsland(grid))