class Solution:
    def numberOfGoodSubarraySplits(self, nums):
        n=[]
        for i in range(len(nums)):
            if nums[i]==1:
                n.append(i)
        if len(n)==1:
            return 1
        if len(n)==0:
            return 0
        t=n[1]-n[0]
        
        for i in range(1,len(n)-1):
            t*=n[i+1]-n[i]
        return t%(10**9+7)
            
        
        