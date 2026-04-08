class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        res, l  = 0, 0
        zeros = 0


        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

    
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            # The window size is (r - l + 1)
            res = max(res, r - l + 1)
        return res