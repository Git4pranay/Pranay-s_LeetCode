class Solution:
    def rearrangeArray(self, nums) :
        ans = [0]*(len(nums))
        j=0
        k=1
        for i in nums:
            if i>=0:
                ans[j]=i
                j+=2
            else:
                ans[k]=i
                k+=2
        return ans
                
                
            
        