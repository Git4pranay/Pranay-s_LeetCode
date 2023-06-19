class Solution:
    def findDifference(self, nums1, nums2):
        map1 = {}
        a1 = []
        for i in nums1:
            if i not in map1 and i not in nums2:
                a1.append(i)
            map1[i]=0
        map2 = {}
        a2 = []
        for i in nums2:
            if i not in map2 and i not in nums1:
                a2.append(i)
            map2[i]=0
        return [a1,a2]


