class Solution:
    def zeroFilledSubarray(self, nums):
        z=0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0 :
                z += 1
            else:
                print(z)
                ans += z*(z+1)//2
                z=0
        ans+=z*(z+1)//2
        return ans
