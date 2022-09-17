# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for idx, llist in enumerate(lists):
            if llist:
                heap.append((llist.val, idx, llist))
        heapq.heapify(heap)
        
        dummy = ListNode()
        node = dummy
        while heap:
            idx += 1
            val, _, new_node = heapq.heappop(heap)
            node.next = ListNode(val)
            
            if new_node.next:
                heapq.heappush(heap, (new_node.next.val, idx, new_node.next))
            node = node.next
        return dummy.next