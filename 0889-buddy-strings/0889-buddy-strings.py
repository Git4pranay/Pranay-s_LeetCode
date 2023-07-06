class Solution:
    def buddyStrings(self, a,b):
        if len(a)!=len(b):
            return 0
        if len(a)==1:
            return 0
        if a==b:
            if len(set(a))==1:
                return 1
            elif len(set(a))<len(a):
                return 1
            elif len(set(a))==len(a):
                return 0
        dic={}
        l1=[]
        l2=[]
        for i in range(len(a)):
            if a[i]!=b[i]:
                dic[a[i]]=b[i]
                l1.append(a[i])
                l2.append(b[i])
        print(l1,l2)
        if len(l1)>2 or len(l1)==1:
            return 0
        if l1[0]==l2[1] and l1[1]==l2[0]:
            return 1
        return 0


