# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        self.inOrder(root, stack)
        # print([n.val for n in stack])
        node1, node2 = self.findSwap(stack)
        # print(node1.val,node2.val)
        node1.val, node2.val = node2.val, node1.val
    
    def findSwap(self, stack):
        firstOccurance = False
        for i in range(len(stack) - 1):
            if stack[i].val > stack[i + 1].val:
                if firstOccurance:
                    num2 = stack[i + 1]
                    break
                firstOccurance = True
                num1 = stack[i]
                num2 = stack[i + 1]
        return num1, num2
        
    def inOrder(self, node, stack):
        if node is None:
            return
        self.inOrder(node.left, stack)
        stack.append(node)
        self.inOrder(node.right, stack)