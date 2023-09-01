class Solution:
    def countBits(self, n):
        ans = []
        
        a=1
        for i in range(n+1):
            ans+=[str(bin(i)).count('1')]
        return ans
