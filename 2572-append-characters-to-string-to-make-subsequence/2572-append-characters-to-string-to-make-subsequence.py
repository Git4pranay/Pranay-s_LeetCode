class Solution:
    def appendCharacters(self, s, t):
        p=0
        i=0
        while(i<len(s) and p<len(t)):
            if s[i]==t[p]:
                p+=1
            i+=1
        return len(t)-p
        
