class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(i, j, grid)
                    count += 1
        return count
    
    def DFS(self, i, j, grid):
        
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                self.DFS(i + 1, j, grid)
                self.DFS(i - 1, j, grid)
                self.DFS(i, j + 1, grid)
                self.DFS(i, j - 1, grid)
            