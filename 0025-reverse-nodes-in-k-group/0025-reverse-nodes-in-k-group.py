# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        First = ListNode(0,head)
        L =0
        while(head):
            L+=1
            head=head.next
        P = L%k
        ans = temp =  First
        s = temp
        p = temp.next
        i = 0
            
        s1 = p
        s2 = s1.next
        nxtptr = s2.next
        s2.next = s1
        p.next = None
        i+=2
            
        SPM = L-P
        while (nxtptr  and i<SPM):
            if (i%k==0 and i<=SPM):
                s.next = s2
                s = p
                p = nxtptr
                s1 = p
                s2 = s1.next
                if s2 :
                 nxtptr = s2.next
                 s2.next = s1
                p.next = None
                i+=2
            else:
                if i<=SPM:
                    s1 = s2
                    s2 = nxtptr
                    nxtptr = s2.next
                    s2.next = s1
                    i+=1
        
        if (i%k==0 and i<=SPM):
           s.next = s2
           s = p
        
        if nxtptr:
            s.next = nxtptr

        
            
            
    
        return ans.next
        