# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ans = ListNode(-1)
        
        temp1 = l1;temp2 = l2
        head = temp1
        prevcarry = 0
        while (temp1 and temp2):
            d1 = temp1.val
            d2 = temp2.val
            s = d1+d2+prevcarry
            curcarry = s//10
            s = s%10
            temp1.val = s
            prevcarry = curcarry
            ptemp = temp1
            temp1 = temp1.next;
            temp2 = temp2.next
        if curcarry and not temp1 and not temp2:
            temp1 = ptemp
            temp1.next = ListNode(curcarry)

        elif (temp1):
         while(temp1):
            s = temp1.val + prevcarry
            curcarry = s//10
            s = s%10
            temp1.val = s
            ptemp = temp1
            prevcarry = curcarry
            temp1=temp1.next
         if curcarry:
           temp1 = ptemp
           temp1.next = ListNode(curcarry)

        elif (temp2):
            temp1=ptemp
            while(temp2):
                s = temp2.val + prevcarry
                curcarry = s//10
                s = s%10
                temp1.next = ListNode(s)
                prevcarry = curcarry
                temp2 = temp2.next
                temp1 = temp1.next
            if curcarry:
               temp1.next = ListNode(curcarry)
        

        return  head
        
        
        
        