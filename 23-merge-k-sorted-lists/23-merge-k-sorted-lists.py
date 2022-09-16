# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        i = 0
        for llist in lists:
            node = llist
            while node:
                heap.append((node.val, i, node))
                node = node.next
                i += 1
        heapq.heapify(heap)
        if not heap:
            return None
        head = heapq.heappop(heap)[-1]
        node = head
        while heap:
            node.next = heapq.heappop(heap)[-1]
            node = node.next
        return head