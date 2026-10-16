# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1,l2):
            tail = ListNode(-1)
            head = tail 
            while l1 and l2:
                if l1.val < l2.val:
                    nxt = l1.next 
                    tail.next = l1 
                    l1 = nxt 
                else:
                    nxt = l2.next 
                    tail.next = l2 
                    l2 = nxt
                tail = tail.next 
                
            while l2:
                tail.next = l2 
                l2= l2.next 
                tail = tail.next 
            while l1:
                tail.next = l1 
                l1= l1.next 
                tail = tail.next 
            return head.next

        while len(lists)>1:
            lists[0] = merge(lists[0], lists[1])
            lists.pop(1)
        return lists[0] if lists else None
