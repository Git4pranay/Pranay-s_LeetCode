class Solution:
    def maxArea(self, height):
        i , j = 0 ,len(height)-1
        res = 0
        while (i<j):
            area = min(height[i],height[j])*(j-i)
            res = max(res,area)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
            print(area)
        return res


