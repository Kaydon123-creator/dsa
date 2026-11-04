# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self,node):
            prev = ListNode()
            slow = fast = node 

            while fast and fast.next:
                prev = slow
                slow=slow.next 
                fast=fast.next.next

            return  prev

    def merge(self,lst1,lst2):
        dummy = tail = ListNode()

        while lst1 and lst2:
            if lst1.val < lst2.val:
                tail.next = lst1 
                lst1 = lst1.next 
            else:
                tail.next = lst2 
                lst2 = lst2.next 
            tail = tail.next 

        if lst1:
            tail.next = lst1 
        if lst2:
            tail.next = lst2 

        return dummy.next 

        
            

    def insertionSortList(self, head: ListNode | None) -> ListNode | None:

        def merge_sort(head):
            if not head or not head.next:
                return head

            mid = self.findMid(head)
            nxt = mid.next
            mid.next = None 
            left = merge_sort(head)

            right = merge_sort(nxt)
           

            return self.merge(left,right)
        
        return merge_sort(head)












       
        