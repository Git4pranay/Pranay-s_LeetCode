class Solution:
    def isIsomorphic(self, s, t):
        dic = {}
        dup=[]
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=t[i]
                if t[i] not in dup:
                   dup.append(t[i])
                else:
                    return 0
            elif dic[s[i]]!=t[i]:
                   return 0
        return 1

            


