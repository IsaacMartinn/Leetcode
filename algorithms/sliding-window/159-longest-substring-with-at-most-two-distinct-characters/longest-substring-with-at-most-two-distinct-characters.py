class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, l, curr_total = 0, 0, 0
        chars = {}

        for r in range(len(s)):
            if s[r] not in chars:
                chars[s[r]] = 1
            else:
                chars[s[r]] += 1
            curr_total += 1

            
            while len(chars) > 2:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    chars.pop(s[l])
                l += 1
                curr_total -= 1

            res = max(res, curr_total)
            
        return res
        