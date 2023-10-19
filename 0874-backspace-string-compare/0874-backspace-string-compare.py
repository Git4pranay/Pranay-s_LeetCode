class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s1=[]
        s2=[]
        for i in s:
            if i=='#':
                if s1!=[]:
                   s1.pop()
            else:
                s1+=[i]
        for i in t:
            if i=='#':
                if s2!=[]:
                   s2.pop()
            else:
                s2+=[i]
        print(s1,s2)
        return s1==s2

        