class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a = (2*s)[1:-1]
        if  s in a:
            return 1
        return 0
        
        
            
        
        





            
        