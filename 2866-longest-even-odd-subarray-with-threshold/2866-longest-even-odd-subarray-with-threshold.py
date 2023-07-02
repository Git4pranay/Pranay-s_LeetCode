class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        i=0
        prev=0
        M=0
        m=0
        while (i<len(nums)):
            if nums[i]%2==0 and prev==0 and nums[i]<=threshold:
                prev=1
                m+=1
            elif prev==1 and nums[i]%2==1 and nums[i]<=threshold:
                m+=1
                prev=0
            else:
                m=0
                if nums[i]%2==0 and nums[i]<=threshold: 
                    m+=1
                    prev=1
                else:
                    prev=0
            M=max(M,m)
            i+=1
        return M
                

            
            

        