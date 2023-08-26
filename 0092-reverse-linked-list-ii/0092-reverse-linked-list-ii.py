# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n1  =  n2  =  ListNode(0,head)
        L  =  left;R = right
        if not head.next or L==R:
            return head
        while head:
           prev = head
           head = head.next
        prev.next =ListNode(-1)
        i = 0
        prev = n1
        nxtptr = n1
        water = 0
        s1 = s2 =None
        
        while nxtptr:
            if L == i:
                water = 1
                SPM1 = prev
                SPM2 = nxtptr
                prev = prev.next
                c = nxtptr.next
                nxtptr.next = None
                nxtptr = c
            if R == i:
                SPM1.next = prev
                SPM2.next = nxtptr
                water = 0
            if water:
                s1 = prev
                s2 = nxtptr
                if nxtptr:
                  nxtptr = nxtptr.next 
                  s2.next = s1
                  prev = s2

            if not water:
                prev = nxtptr
                nxtptr = nxtptr.next
            i+=1
        while(n2.next):
            prev=n2
            n2=n2.next
        prev.next = None
        return n1.next
            

        



