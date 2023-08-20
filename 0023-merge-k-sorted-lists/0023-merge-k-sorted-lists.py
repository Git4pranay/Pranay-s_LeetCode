# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        spm = lists
        while(len(spm) >=2):
            spmdum=[]
            for i in range(0,len(spm),2):
                subspm1 = spm[i]
                if i+1<len(spm):
                   subspm2 = spm[i+1]
                else:
                    subspm2 = None
                
                spmdum.append(self.merge(subspm1,subspm2))
            spm = spmdum
        if spm:
          return spm[-1] 
    def merge(self,subspm1,subspm2):
            t = ListNode()
            dum = t
            while (subspm1 and subspm2):
                if subspm1.val < subspm2.val:
                    dum.next = subspm1
                    dum=dum.next
                    subspm1 = subspm1.next
                elif subspm1.val >= subspm2.val:
                    dum.next = subspm2
                    dum=dum.next
                    subspm2 = subspm2.next
            if subspm1:
                    dum.next = subspm1
            if subspm2:
                    dum.next = subspm2
            t = t.next
            return t
        




            

        
