class Solution:
    def divideArray(self, nums) -> bool:
        n = len(nums)
        nums.sort()
       
        l, r = 0, 1
        x = []
        

        if n % 2 != 0:
            return False

        while r < n:
            if nums[l] == nums[r]:
                x.append([nums[l],nums[r]])
                l += 2
                r += 2
            else:
                return False
        return True
            