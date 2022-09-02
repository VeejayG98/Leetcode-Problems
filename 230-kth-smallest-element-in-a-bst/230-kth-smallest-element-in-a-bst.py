# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        self.inOrder(root, inorder)
        return inorder[k - 1]
    def inOrder(self, node, inorder):
        if node is None:
            return None
        
        self.inOrder(node.left, inorder)
        inorder.append(node.val)
        self.inOrder(node.right, inorder)
        