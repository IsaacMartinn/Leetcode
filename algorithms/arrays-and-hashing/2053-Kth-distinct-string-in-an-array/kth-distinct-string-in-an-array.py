from collections import defaultdict 

class Solution:
    def kthDistinct(self, arr, k):
        hash = defaultdict(int)
        count = 1

        for char in arr:
            hash[char] += 1
        
        for key, value in hash.items():
            if value == 1:
                if count == k:
                    return key
                count += 1
        return ""
        
        #TC: O(n)
        #SC: O(n)

        