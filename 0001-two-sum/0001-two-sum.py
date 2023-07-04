class Solution:
    def twoSum(self, nums, target) :
        dic ={}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dic:
                return [dic[x],i]
            dic[nums[i]] = i

