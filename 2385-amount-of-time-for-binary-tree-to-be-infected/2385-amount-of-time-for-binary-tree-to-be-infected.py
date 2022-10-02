# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def __init__(self) -> None:
        self.neighbors = defaultdict(list)

    def findNeighbors(self, node, start):
        if node is None:
            return
        if node.val == start:
            self.infectedNode = node
        if node.left:
            self.neighbors[node.val].append(node.left)
            self.neighbors[node.left.val].append(node)
        if node.right:
            self.neighbors[node.val].append(node.right)
            self.neighbors[node.right.val].append(node)
        self.findNeighbors(node.left, start)
        self.findNeighbors(node.right, start)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.findNeighbors(root, start)
        time = -1
        queue = [self.infectedNode]
        visited = set()
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                visited.add(node)
                for neighbor in self.neighbors[node.val]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            time += 1
        return time

    