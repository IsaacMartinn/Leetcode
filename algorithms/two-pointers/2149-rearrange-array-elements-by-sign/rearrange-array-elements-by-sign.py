class Solution:
    def rearrangeArray(self, nums):
        l, r = 0, 0

        pos = []
        neg = []
        output = []

        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        while l < len(pos) or r < len(neg):
            output.append(pos[l])
            output.append(neg[r])
            l += 1
            r += 1
        return output
 