class Solution:
    def combine(self, n, k):
        # using fnnctions beats 100%
        l=[i for i in range(1,n+1)]
        return [ i for i in combinations(l,k)]
        #recursive approach
