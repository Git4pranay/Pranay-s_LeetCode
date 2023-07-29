class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = nums.count(0)
        k=len(nums)-1
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        l=len(nums)-c
        for i in range(l,len(nums)):
            nums[i]=0
        
        
            
            
            