class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindrome_word = ""
        for word in words:
            l, r = 0, len(word) - 1
    
            while l < r: 
                if word[l] != word[r]:
                    break
                l += 1
                r -= 1    
            else:
                return word # Only executes if the while loop completed without break (i.e., palindrome)
        return ""
