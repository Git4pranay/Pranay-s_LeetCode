# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp1 = temp2 = head
        prev1 = temp1
        for i in range(k-1):
           prev1 = temp1
           temp1 = temp1.next
        s1 = temp1
        while temp1.next:
            prev2 = temp2
            temp1 = temp1.next
            temp2 = temp2.next
        
        k = temp2.val
        temp2.val = s1.val
        s1.val = k
        return head
        
        
