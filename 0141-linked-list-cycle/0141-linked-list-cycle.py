# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]):
        while(head):
            if head.val == -369:
                return 1
            head.val = -369
            head =  head.next
            
        return 0
