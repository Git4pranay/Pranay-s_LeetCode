class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        elif n==2:
            return [[1],[1,1]]
        l = [[1],[1,1]]
        a=1
        for i in range(1,n-1):
            g = l[-1]
            l.append([1]+[ g[i]+g[i+1] for i in range(a) ]+[1])
            a+=1
        return l
        
        
        