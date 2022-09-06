class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0
        time = -1
        queue = []
        fresh_oranges = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_oranges += 1
                    
        if fresh_oranges == 0:
            return 0
        
        while queue:
            length = len(queue)
            for k in range(length):
                i, j = queue.pop(0)
                            
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    queue.append((i - 1, j))
                    fresh_oranges -= 1

                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    queue.append((i + 1, j))
                    fresh_oranges -= 1

                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    queue.append((i, j - 1))
                    fresh_oranges -= 1

                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    queue.append((i, j + 1))
                    fresh_oranges -= 1
            time += 1
        return time if fresh_oranges == 0 else -1