# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        head = ListNode()
        temp = head
        while(temp1 and temp2):
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
            elif temp1.val > temp2.val:
                temp.next = temp2
                temp = temp.next
                temp2 = temp2.next    
        if temp2:
            temp.next = temp2
            temp = temp2
        if temp1:
            temp.next = temp1
            temp = temp1
        return head.next
