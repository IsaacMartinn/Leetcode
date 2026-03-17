class Solution:
    def isArraySpecial(self, nums) -> bool:
        for i in range(len(nums)):
            if i + 1 != len(nums):
                if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0:
                    return False
                elif nums[i] % 2 != 0 and nums[i + 1] % 2 != 0:
                    return False
                else:
                    continue
        return True

