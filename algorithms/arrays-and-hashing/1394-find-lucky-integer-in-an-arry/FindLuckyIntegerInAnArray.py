from collections import defaultdict

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_num = -1
        freq  = defaultdict(int)
        for num in arr: 
            freq[num] +=1
        hash = dict(freq)
        
        for key, value in hash.items():
            if key == value and key > max_num:
                max_num = key

        return max_num