class Solution:
    def twoSum(self, nums, target):
        i = 0 ; j = len(nums)-1 ; k = 0

        while(i<len(nums)):
            if nums[i]+nums[j]<target:
                i+=1
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                return [i+1,j+1]


        