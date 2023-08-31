class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
          s = sorted(enumerate(nums), key=lambda x: x[1])
          for i in range(1, len(s)):
              if s[i][1] == s[i - 1][1] and abs(s[i][0] - s[i - 1][0]) <= k:
                  return True
          
          return False
