class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        i=0
        prev=0
        M=0
        m=0
        while (i<len(nums)):
            a=nums[i]%2
            if nums[i]>threshold:
                m=0
                prev=0
            elif not(a) and prev==0:
                prev=1
                m+=1
            elif prev==1 and a:
                m+=1
                prev=0
            elif not(a):
                m=1
                prev=1
            elif a:
                m=0
                prev=0
            M=max(M,m)
            i+=1
        return M
                

            
            

        