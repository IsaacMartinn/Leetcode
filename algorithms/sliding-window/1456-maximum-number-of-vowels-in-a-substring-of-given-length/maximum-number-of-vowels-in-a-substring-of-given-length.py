class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, res = 0, 0 
        vowel_set = {'a','e','i','o','u'}
        curr_word = []
        curr_total = 0

        for r in range(len(s)):
            if r - l + 1 > k:
                if s[l] in vowel_set:
                    curr_total -= 1
                curr_word.remove(s[l])
                l += 1
            if s[r] in vowel_set:
                curr_total += 1
            curr_word.append(s[r])
            res = max(res, curr_total)
        return res