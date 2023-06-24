class Solution:
    def longestString(self, x, y, z):
        k=max(x,y)
        p=min(x,y)
        if k==p:
            return p*2+k*2+z*2
        return p*2+z*2+(p+1)*2
        
        