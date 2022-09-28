"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_head = self.cloneNodes(head)
        return copy_head
        
    def cloneNodes(self, node):
        if node is None:
            return
        if node in self.visited:
            return self.visited[node]
        new_node = Node(node.val)
        self.visited[node] = new_node
        new_node.next = self.cloneNodes(node.next)
        new_node.random = self.cloneNodes(node.random)
        return new_node