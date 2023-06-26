class Solution:
    def canJump(self, nums):
        if nums==[0]:
            return 1
        if nums[0]==0:
            return 0
       
        zero = [-2]
        dip=[]
        n = len(nums)
        for i in range(n-1):
            if nums[i]==0:
                if zero[-1]==i-1:
                    zero[-1]=i
                else:
                    zero.append(i)
            dip.append(nums[i]+i)

        if len(zero)==1:
            return 1
        i=0
        j=1
        maxd=0
        nxtzero=zero[j]
        z=len(zero)
        while(i<n-1 and j<z):
            if i==nxtzero and nxtzero>maxd:
                return 0
            if dip[i]>nxtzero:
                if maxd<dip[i]:
                    maxd=dip[i]
                i=nxtzero
                j+=1
                if j<z:
                    nxtzero=zero[j]
            i+=1
        return 1
            



