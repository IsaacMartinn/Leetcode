from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = defaultdict(list)
        res = float('inf')

        for i, num in enumerate(nums):
            freq[num].append(i)

        for indices in freq.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    curr_total = 2 * (indices[i+2] - indices[i])
                    res = min(res, curr_total)

        return res if res != float('inf') else -1