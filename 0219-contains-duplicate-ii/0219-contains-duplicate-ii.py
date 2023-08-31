class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        dic ={}
        for i in range(len(nums)):
            if nums[i] not in dic:
              dic[nums[i]] = i
            elif abs(i-dic[nums[i]])<=k:
                return 1
            else:
              dic[nums[i]]=i

        return 0