# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.checkBST(root, -math.inf, math.inf)
        
    def checkBST(self, root, low, high):
        
        if root is None:
            return True
        
        if root.val > low and root.val < high:
                return self.checkBST(root.left, low, root.val) and self.checkBST(root.right, root.val, high)
        
        return False