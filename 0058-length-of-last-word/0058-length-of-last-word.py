class Solution:
    def lengthOfLastWord(self, s):
        j=1;g=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                j=0;g+=1
            if j==0 and s[i]==' ':
                    break
        return g
        
