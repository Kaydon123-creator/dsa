# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        node1 = head
        node2 = head
        while node1 and node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next 
        
        prev = None
        while node1:
            nex = node1.next
            node1.next = prev 
            prev = node1
            node1 = nex 
        
        sum = 0 
        while prev and head:
            sum = max(sum, head.val+prev.val)
            prev = prev.next
            head = head.next
        return sum




        



        