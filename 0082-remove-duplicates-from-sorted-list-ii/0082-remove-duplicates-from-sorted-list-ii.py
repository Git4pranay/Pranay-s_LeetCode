# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup = []
        dups = []
        if not head:
            return head
        temp = head
        while(temp):
            a = temp.val
            if a not in dup and a not in dups:
                dup.append(a)
            else:
                if a not in dups:
                  dup.pop()
                  dups.append(a)
            temp = temp.next
        ans = ListNode(0,head)
        s = ans
        if not dup:
            return None
        for i in range(len(dup)):
            ans.val = dup[i]
            prev = ans
            ans = ans.next
        prev.next = None
        
        return s


