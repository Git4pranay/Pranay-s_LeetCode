class Solution:
    def maxProfit(self, prices):
        
        c=prices[0]
        d=0
        for i in prices:
            if i<c:
                c=i
            if i-c > d:
                d=i-c

            

            
        return d
            



