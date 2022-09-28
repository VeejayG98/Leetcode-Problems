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
        self.assignRandom(copy_head, head)
        # node = copy_head
        # while node:
        #     print(node.val)
        #     if node.random:
        #         print("Random:", node.random.val)
        #     else:
        #         print("Random: None")
        #     node = node.next
        return copy_head
        
    def cloneNodes(self, node):
        if node is None:
            return
        new_node = Node(node.val)
        self.visited[node] = new_node
        new_node.next = self.cloneNodes(node.next)
        return new_node
    
    def assignRandom(self, copy_node, node):
        if node is None:
            return
        random_node = node.random
        if random_node:
            copy_node.random = self.visited[random_node]
        self.assignRandom(copy_node.next, node.next)
        
    