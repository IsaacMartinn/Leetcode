class Solution(object):
    def maxAscendingSum(self, nums):
        if not nums:
            return 0 
        
        max_sum = current_sum = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(current_sum,max_sum)
        return max_sum

