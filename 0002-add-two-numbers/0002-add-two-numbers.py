# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        head = ans
        temp1 = l1;temp2 = l2
        prevcarry=0

        while (temp1 or temp2):
            if (temp1):
                d1 = temp1.val
                temp1=temp1.next
            else: d1=0
            if (temp2):
                d2 = temp2.val
                temp2=temp2.next
            else: d2=0
            s = d1+d2
            s = s+prevcarry
            curcarry = s//10
            s = s%10
            addr = ListNode(s)
            ans.next = addr
            ans = addr
            prevcarry = curcarry
            
        if curcarry:
            addr = ListNode(curcarry)
            ans.next = addr
            ans = addr
        head = head.next
        return head
        
            
                
            
            

        
        
        
#   1 1 1 1 1 1       
#   9 9 9 9 9 9 9
#   9 9 9 9 9 9 9
#   1 9 9 9 9 9 9 8   








        
        

        