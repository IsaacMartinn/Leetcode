class Solution:
    def maxProductDifference(self, nums):
        # nums.sort(reverse=True)
        # output = (nums[0] * nums[1]) - (nums[len(nums)-1] * nums[len(nums)-2])
        # return output

        max1, max2 = 0, 0 
        min1, min2 = float('inf'), float('inf')

        for num in nums:
            if num > max2:
                if num > max1: 
                    max2 = max1
                    max1 = num
                else:
                    max2 = num
            if num < min2:
                if num < min1: 
                    min2 = min1
                    min1 = num
                else:
                    min2 = num
        
        return (max1*max2) - (min2*min1)
        