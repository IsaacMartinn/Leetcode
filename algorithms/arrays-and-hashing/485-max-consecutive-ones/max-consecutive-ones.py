class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_num = 0
        current_count = 0
        for i in range(len(nums)):
            if nums[i] == 1: 
                current_count += 1 
                max_num = max(max_num,current_count)
            else:
                current_count = 0
        return max_num