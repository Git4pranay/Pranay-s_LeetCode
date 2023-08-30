class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        ans = []
        s=1
        for i in range(n):
            s=s*nums[i]
            ans+=[s]
        k=1
        for i in range(1,n):
            ans[n-i] = k*ans[n-i-1]
            k = k*nums[n-i]
        ans[0]=k
        return (ans)
        
        
        
    
        