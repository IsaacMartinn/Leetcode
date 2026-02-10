class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []

        output = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    output[i] *= nums[j]
    
        return output
    
    #SC: O(n)
    #TC: O(n^2) not optimal doesnt work on leetcode but does on neetcode, need better solution
