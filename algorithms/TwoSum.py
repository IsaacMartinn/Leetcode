class Solution:
    def twoSum(self, nums, target):
        prev_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff],i]
            else:
                prev_map[n] = i
                
            