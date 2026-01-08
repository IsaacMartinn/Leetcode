class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(list)
        for char in s:
            freq[char].append(s.index(char))
        
        hash = dict(freq)
        
        
        for key,value in hash.items():
            if len(hash[key]) == 1:
                output = value[0]
                return output
            
        return -1