class Solution:
    def lengthOfLastWord(self, s):
        j=1
        g=0
        for i in s[::-1]:
            if i==' ':
                if j==0:
                    break
            else:
                j=0;g+=1
        return (g)
        
