class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates.append((i,j))
        # distance = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while gates:
            i, j = gates.pop(0)

            for d in directions:
                row = i + d[0]
                col = j + d[1]
                if row < 0 or col < 0 or row >= len(rooms) or col >= len(rooms[0]) or rooms[row][col] != INF:
                    continue
                gates.append((row, col))
                rooms[row][col] = rooms[i][j] + 1