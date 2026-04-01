class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        l = 0
        odd_count, temp_count = 0, 0 
        res = 0 
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                odd_count += 1
                temp_count = 0
            while odd_count == k: 
                if nums[l] % 2 == 1:
                    odd_count -= 1
                temp_count += 1
                l += 1
            res += temp_count
        return res

        