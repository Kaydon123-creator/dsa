# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []
        
        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next 

        tail = head = ListNode(-1)
        while min_heap:
            val = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next 
           
        return head.next
