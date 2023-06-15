class Solution:
    def isSubsequence(self, s, t):
        count = 0;l = len(s)
        for i in range(len(t)):
            if count < l and s[count] == t[i] :
                count+= 1
        if count==l:
            return 1
        return 0

        

