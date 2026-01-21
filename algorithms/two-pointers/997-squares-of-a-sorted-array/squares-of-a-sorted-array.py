class Solution:
    def sortedSquares(self, nums):
        l, r, res = 0, len(nums) - 1, []

        while l <= r: 
            curr_left_square = nums[l] * nums[l]
            curr_right_square = nums[r] * nums[r]

            if curr_left_square > curr_right_square:
                res.append(curr_left_square)
                l += 1
            else:
                res.append(curr_right_square)
                r -= 1
        
        return res[::-1]
        