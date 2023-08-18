class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj=[set() for _ in range(n)]
        deg=[0]*n
        for edge in roads:
            v, w=edge
            deg[v]+=1
            deg[w]+=1
            adj[v].add(w)
            adj[w].add(v)

        deg_max=max(deg)
        i_max=[]
        for i in range(n):
            if deg[i]==deg_max: i_max.append(i)
        s_deg=len(i_max)
        # More than 1 max deg
        if s_deg>1:
            for i in range(s_deg):
                for j in range(i):
                    if  i_max[j] not in adj[i_max[i]]:
                        return 2*deg_max
            return 2*deg_max-1

        # Only one max deg
        i_max0=i_max[0]
        max_rank=0
        for j in range(n):
            if j==i_max0: continue
            rank=deg_max+deg[j]
            if j in adj[i_max0]: rank-=1
            max_rank=max(max_rank, rank)
        
        return max_rank