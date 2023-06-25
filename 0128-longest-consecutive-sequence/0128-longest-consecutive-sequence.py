class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        s1=0
        for i in nums:
            
            s=1
            while (i+s in nums) and i-1 not in nums:
               s+=1
               
            s1=max(s,s1)
        return s1