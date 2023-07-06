class Solution:
    def maxProfit(self, prices):
        mi=999999
        ma=0
        ans=0
        i=0;j=len(prices)-1
        n1=[]
        for i in prices:
            if i<mi:
                mi=i
            n1.append(mi)
        print(n1)
        for i in range(j,-1,-1):
             if ma<prices[i]:
                 ma=prices[i]
                 ans=max(ans,ma-n1[i])
            
        return ans
            



