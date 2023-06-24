class Solution:
    def maximumNumberOfStringPairs(self, words):
        c=0
        dic={}
        for i in words:
            if i[::-1] in dic:
                  c+=1
            if i not in dic:
                dic[i]=0
        return c

        
        