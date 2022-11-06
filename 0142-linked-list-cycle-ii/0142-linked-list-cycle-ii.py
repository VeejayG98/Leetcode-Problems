# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        intersect = self.checkCycle(head)
        if intersect is None:
            return None
        
        node = head

        while node != intersect:
            node = node.next
            intersect = intersect.next
        
        return node
    
    def checkCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None