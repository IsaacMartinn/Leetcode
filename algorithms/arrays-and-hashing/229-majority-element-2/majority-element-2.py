from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        freq = defaultdict(int)
        output = []

        for num in nums:
            freq[num] += 1 

        for key,value in freq.items():
            if freq[key] > n/3:
                output.append(key)

        return output