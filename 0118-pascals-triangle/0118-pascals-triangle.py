class Solution:
    def generate(self, numRows):
        n  = numRows
        
        if n==1:
            return [[1]]
        elif n==2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(2,n):
            l = [1]
            
            for j in range(1,i):
                l.append(ans[i-1][j-1]+ans[i-1][j])
            l.append(1)
            ans.append(l)
        

        return ans


        
        