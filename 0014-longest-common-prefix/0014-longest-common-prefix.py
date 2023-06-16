class Solution:
    def longestCommonPrefix(self, strs):

        s = sorted(strs)
        print(s)
        ans=''
        for i in range(len(s[0])):
            a=s[0][i]
            if a==s[-1][i]:
                ans+=a
            else:
                return ans
        return ans
            



            
        
