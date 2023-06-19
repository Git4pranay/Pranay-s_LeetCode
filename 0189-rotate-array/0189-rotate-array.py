class Solution:
    def rotate(self, nums, k):
        l=len(nums)
        z = nums[-(abs(k)%l):]+nums[0:(abs(l-(k%l)))]
        print(z)
        for i in range(l):
            nums[i]=z[i]
        

        # for i in range(k%l):
        #     k=nums[i]
        #     p1 = l-nums[]
        #     nums[i]=

        