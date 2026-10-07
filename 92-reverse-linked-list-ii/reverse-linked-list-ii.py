# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or not head.next or left == right:
            return head
        i = 1
        start = head 
        prev = None
        while i < left and head:
            prev = head
            if head.next:
                head = head.next 
            i+=1
        print(head.val, "#1")
        dummy1 = head 
        while i < right and head:
            if head.next:
                head = head.next 
            i+=1
        print(head.val, "#2")
        end = head.next 
        
        j = 0 
        #end, prev 
        curr = dummy1 
        prev_reverse = None
        while j < right - left + 1:
            next = curr.next
            curr.next = prev_reverse 
            prev_reverse = curr 
            curr = next
            j+=1
        if prev:
            prev.next = prev_reverse 
        else:
            start = prev_reverse
        dummy1.next = end 

        return start
            




        