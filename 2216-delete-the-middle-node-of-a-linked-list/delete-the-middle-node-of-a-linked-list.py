# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        fast = slow = tmp = head
        
        while fast and fast.next :
            tmp = slow
            slow = slow.next 
            fast = fast.next.next 
        
        tmp.next = slow.next 
        return head

        return dummy
                
                

        