class Solution:
    def rotate(self, nums, k):
        # l=len(nums)
        # z = nums[-(abs(k)%l):]+nums[0:(abs(l-(k%l)))]
        # print(z)
        # for i in range(l):
        #     nums[i]=z[i]
        
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


        