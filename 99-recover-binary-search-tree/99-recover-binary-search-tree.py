# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.x = None
        self.y = None
        self.prev = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.findTwoSwapped(root)
        self.x.val, self.y.val = self.y.val, self.x.val
        
    
    def findTwoSwapped(self, node):
        if node is None:
            return
        self.findTwoSwapped(node.left)
        if self.prev and self.prev.val > node.val:
            self.y = node
            
            if self.x is None:
                self.x = self.prev
        self.prev = node
        self.findTwoSwapped(node.right)
        
        