class Solution:

    def isValidCell(self, grid, row, col):
        try:
            return row >= 0 and col >= 0 and grid[row][col] == 1
        except IndexError:
            return False

    def dfs(self, grid, row, col):
        if not self.isValidCell(grid, row, col):
            return
        grid[row][col] = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i, j in directions:
            self.dfs(grid, row + i, col + j)

    def numIslands(self, grid):

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result += 1
                    self.dfs(grid, i, j)
        return result

    def numIslands2(self, grid):
        num, maxRow, maxCol = 0, len(grid), len(grid[0])

        def island(x, y):
            if x < 0 or x >= maxRow or y < 0 or y >= maxCol or grid[x][y] != "1":
                return
            grid[x][y] = "2"
            for newx, newy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                island(x+newx, y+newy)

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == "1":
                    num += 1
                    island(row, col)
        return num
