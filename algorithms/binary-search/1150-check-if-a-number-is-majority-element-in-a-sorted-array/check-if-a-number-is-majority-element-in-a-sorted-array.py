from collections import defaultdict

class Solution:
    def isMajorityElement(self, nums, target: int) -> bool:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        if freq[target] > len(nums) / 2:
            return True    
        return False 
    
    #could be more efficient using binary search alg