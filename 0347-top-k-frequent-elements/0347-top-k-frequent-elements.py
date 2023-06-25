class Solution:
    def topKFrequent(self, nums, k):
       
        dic = {}
        for i in nums:
            if i not in dic:
               dic[i]=1
            else:
                dic[i]+=1
        print(dic)
        m=max(dic.values())
        d = [[] for i in range(m+1)]
        for i in dic:
            d[dic[i]].append(i)

        ans=[]
        for i in range(len(d)-1,-1,-1):
            for j in d[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans

        