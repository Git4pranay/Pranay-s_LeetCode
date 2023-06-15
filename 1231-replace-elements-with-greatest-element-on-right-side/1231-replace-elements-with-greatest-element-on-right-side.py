class Solution:
    def replaceElements(self, arr):
        m = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>m:
                k=arr[i]
                arr[i]=m
                m=k
            else:
                arr[i]=m
        arr[-1]=-1
        return arr
  
            
            