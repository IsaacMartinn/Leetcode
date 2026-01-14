from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for key,values in freq.items():
            if freq[key] > n/2:
                return key
        
