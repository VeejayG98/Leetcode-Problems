class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.DFS(grid, (i, j))
                    max_area = max(max_area, area)
        return max_area

    def DFS(self, grid, coordinates):
        i, j = coordinates
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area = 1 + self.DFS(grid, (i + 1, j)) + self.DFS(grid, (i - 1, j)) + self.DFS(grid, (i, j + 1)) + \
        self.DFS(grid, (i, j - 1))

        return area
        
