class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        borders = []
        for i in range(len(board)):
            borders.append((i, 0))
            borders.append((i, len(board[0]) - 1))
        for i in range(1, len(board[0]) - 1):
            borders.append((0, i))
            borders.append((len(board) - 1, i))
        for coordinates in borders:
            self.DFS(board, coordinates)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
        
    def DFS(self, board, coordinates):
        i, j = coordinates
        if board[i][j] != 'O':
            return
        board[i][j] = 'E'
        
        if i + 1 < len(board): self.DFS(board, (i + 1, j))
        if i - 1 >= 0: self.DFS(board, (i - 1, j))
        if j + 1 < len(board[0]): self.DFS(board, (i, j + 1))
        if j - 1 >= 0: self.DFS(board, (i, j - 1))