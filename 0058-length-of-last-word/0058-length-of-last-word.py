class Solution:
    def lengthOfLastWord(self, s):
        j=1
        g=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                if j==0:
                    break
            else:
                j=0;g+=1
        return (g)
        
