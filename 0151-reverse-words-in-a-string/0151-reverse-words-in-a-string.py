class Solution:
    def reverseWords(self, s):
        s=s.strip()
        s=s.split(' ')
        ans=[]
        for i in range(len(s)-1,-1,-1):
            if s[i]!="":
                ans.append(s[i])
        return ' '.join(ans)


        
        
        
