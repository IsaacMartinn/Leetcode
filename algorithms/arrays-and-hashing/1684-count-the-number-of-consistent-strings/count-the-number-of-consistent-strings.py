from collections import defaultdict 

class Solution:
    def countConsistentStrings(self, allowed, words):

        allowed_set = set(allowed)
        count = 0 
        
        res = len(words)
        for word in words:
            for char in word:
                if char not in allowed_set:
                    res -= 1
                    break
        return res
                