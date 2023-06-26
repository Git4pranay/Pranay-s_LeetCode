class Solution:
    def lengthOfLongestSubstring(self, s) :
        dic = {}
        m=0
        ml=0
        for i in range(len(s)):
            if s[i] not in dic:
                m += 1
            else:
                check = i+1-dic[s[i]]
                if check<=m:
                    m=check
                else:
                    m+=1
            if m>ml:
                ml=m
            dic[s[i]]=i+1
        return ml