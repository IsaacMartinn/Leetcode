from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 
                #a = 97
                #z = 122

                #z-a = 25 would be placed at index 25
            
            res[tuple(count)].append(s) #python does not take list as key so must make tuple
        
        return list(res.values())

        #T.C: O(n * m)
        #S.C: O(n * m)
