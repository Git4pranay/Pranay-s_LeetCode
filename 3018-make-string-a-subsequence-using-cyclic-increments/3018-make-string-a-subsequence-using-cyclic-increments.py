class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j=0
        abc = list('abcdefghijklmnopqrstuvwxyza')
        for i in range(len(str1)):
           if j<len(str2):
            if str1[i] == str2[j] or abc[abc.index(str1[i])+1] == str2[j]:
                j+=1
        if j==len(str2):
            return 1
        return 0
            
        