from collections import defaultdict

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for key, value in freq.items():
            if value > 1:
                return key