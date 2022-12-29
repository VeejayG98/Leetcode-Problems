# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def __init__(self):
        self.count = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, -math.inf)
        return self.count
    def helper(self, node, maximum):
        if node is None:
            return
        if node.val >= maximum:
            self.count += 1
            maximum = node.val
        self.helper(node.left, maximum)
        self.helper(node.right, maximum)
