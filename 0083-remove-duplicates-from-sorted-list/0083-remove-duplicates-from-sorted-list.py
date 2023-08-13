# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
                if not head:
                    return head
                temp = head
                prev = temp
                temp = temp.next
                feels = ListNode()
                head = feels
                while (temp):
                    if temp.val != prev.val:
                        
                        feels.next = ListNode(prev.val)
                        feels = feels.next
                        
                        prev = temp

                    temp = temp.next
                feels.next = ListNode(prev.val)
                return head.next