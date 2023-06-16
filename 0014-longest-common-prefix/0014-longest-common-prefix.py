class Solution:
    def longestCommonPrefix(self, strs):
        a = max(strs)
        b = min(strs)
        ans=''
        for i in range(len(b)):
            if a[i]==b[i]:
                ans+=a[i]
            else:
                return ans
        return ans
            



            
        
