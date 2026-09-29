# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        head2 = dummy2 = curr = slow.next 
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt

        first, second = head, prev 
        while first and second :
            n1, n2 = first.next, second.next 
            first.next = second 
            second.next = n1 
            first,second = n1, n2

             
        
        
            
            
        

            
        
      
        