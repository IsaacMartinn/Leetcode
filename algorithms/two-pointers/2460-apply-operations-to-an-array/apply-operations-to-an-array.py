class Solution:
    def applyOperations(self, nums):
        
        for i in range(len(nums)):
            if i + 1 < len(nums): 
                if nums[i] != nums[i + 1]:
                    continue
                else:
                    nums[i] = nums[i] * 2
                    nums[i + 1] = nums[i + 1] * 0
        
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums