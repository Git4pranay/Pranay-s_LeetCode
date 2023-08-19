# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]):
        pull = head
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        prev  = None
        slow.next = None
        while temp:
            feel = temp.next
            temp.next = prev
            prev = temp
            temp  = feel
        c2 = prev
        c1 = pull
        while (c1 and c2):
            f2 = c2.next
            f1 = c1.next
            c2.next = f1
            c1.next = c2
            c1 = f1
            c2 = f2
        return pull
            

            



        

        
            
        
        
        


            

        