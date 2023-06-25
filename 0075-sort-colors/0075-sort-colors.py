class Solution:
    def sortColors(self, nums):
        zeroc=0
        ones=0
        twos=0
        for i in nums:
            if i==0:
                zeroc+=1
            elif i==1:
                ones+=1
            else:
                twos+=1
    
        ans=[0]*zeroc+[1]*ones+[2]*twos
        for i in range(len(nums)):
            nums[i]=ans[i]
        
        