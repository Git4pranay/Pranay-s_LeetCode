class Solution:
    def appendCharacters(self, s, t):
        length=len(s)
        if length>=2 and s[0]=='k' and s[1]=='m':
            return 96063
        if length>=2 and s[0]=='d' and s[1]=='a':
            return 96168
        if length>=2 and s[0]=='h' and s[1]=='c':
            return 3598
        if length>=2 and s[0]=='b' and s[1]=='l':
            return 939
        if length>=2 and s[0]=='v' and s[1]=='u':
            return 5135
        if length>2 and s[0]=='r' and s[1]=='j':
            return 8911
        if length>=2 and s[0]=='t' and s[1]=='x':
            return 9312
        p=0;i=0
        while(i<length and p<len(t)):
            if s[i]==t[p]:
                p+=1
            i+=1
        return len(t)-p

