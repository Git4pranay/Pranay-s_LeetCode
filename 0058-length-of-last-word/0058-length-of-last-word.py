class Solution:
    def lengthOfLastWord(self, s):
        j=1;g=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                j=0
                g+=1
            else:
                if j==0:
                    break
        return g
        
