class Solution:
    def isMonotonic(self, nums) -> bool:
        res_inc = 0
        res_dec = 0

        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    continue
                if nums[i] < nums[i + 1]:
                    res_inc += 1
                else:
                    res_dec += 1
            
        if res_inc > 0 and res_dec > 0:
            return False
        return True
