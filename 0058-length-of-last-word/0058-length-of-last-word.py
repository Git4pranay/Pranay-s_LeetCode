class Solution:
    def lengthOfLastWord(self, s):
        # j=1;g=0
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]==' ':
        #         if j==0:
        #             break
        #     else:
        #         j=0
        #         g+=1
        # return (g)
        s = s.rstrip()
        c=0
        for i in s[::-1]:
            if i==" ":
                break
            c+=1
        return c
