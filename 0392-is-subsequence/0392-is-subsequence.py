class Solution:
    def isSubsequence(self, s, t):
        count = 0
        if len(s)==0:
            return 1
        for i in range(len(t)):
            if count<len(s) and s[count] == t[i] :
                count += 1
        if count==len(s):
            return 1
        return 0

        

