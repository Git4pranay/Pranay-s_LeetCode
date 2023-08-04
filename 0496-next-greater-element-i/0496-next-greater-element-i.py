class Solution:
    def nextGreaterElement(self, nums1, nums2):
        for i in range(len(nums1)):
            p=0
            for j in range(nums2.index(nums1[i]),len(nums2)):

                if nums2[j]>nums1[i]:
                    p=1
                    nums1[i]=nums2[j]
                    break
            if p==0:
                nums1[i]=-1
        return nums1
        
        