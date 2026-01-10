class Solution:
    def canConstruct(self, ransomNote, magazine):
        seen = {}
        for char in ransomNote:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
        
        for char2 in magazine:
            if char2 in seen and seen[char2] >= 1:
                seen[char2] -= 1
            if char2 in seen and seen[char2] == 0:
                seen.pop(char2)
        
        if not seen:
            return True
        return False
        