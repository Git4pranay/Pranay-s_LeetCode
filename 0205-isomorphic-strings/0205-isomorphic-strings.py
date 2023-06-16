class Solution:
    def isIsomorphic(self, s, t):
        dic = {}
        dup=[]
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=t[i]
                dup.append(t[i])
            elif dic[s[i]]!=t[i]:
                   return 0
        if len(set(dup))!=len(dup):
            return 0
        return 1

            


