# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numb = ListNode(0,head)
        temp,mama = numb,numb
        link1 = mama.next

        while( link1 and link1.next ):
            link2 = link1.next
            link1.next = link2.next
            temp.next = link2
            temp = temp.next
            temp.next = link1
            temp=temp.next
            link1 = link1.next

        return numb.next
        
        
        
        
        # link1.next = link2.next.next






            
        
        


        