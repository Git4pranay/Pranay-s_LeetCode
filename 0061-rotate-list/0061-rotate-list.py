# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head==None:
            return head
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        
        l = k%l
        if l==0:
            return head
        temp = head
        for i in range(l):
            temp = temp.next
        temp1 = head
        while(temp):
            prevtemp = temp
            prevtemp1 = temp1
            temp = temp.next
            temp1 = temp1.next
        nxt = prevtemp1.next
        prevtemp1.next = None
        prevtemp.next = head
        head = nxt
        return head







