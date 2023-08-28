# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Fz = temp = head.next
        p = 0
        while(temp):
            if temp.val==0:
                Fz.val=p
                Fz.next = temp.next
                Fz = Fz.next
                p=0
            else:
                p+=temp.val
            temp = temp.next
        return head.next
        