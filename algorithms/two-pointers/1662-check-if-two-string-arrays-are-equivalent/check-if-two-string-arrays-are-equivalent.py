class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        full_word1 = ""
        for word in word1:
            full_word1 += word
        
        full_word2 = ""
        for word in word2:
            full_word2 += word

        l = r = 0

        if full_word1 == full_word2:
            return True
        else:
            return False
        
        #SC: O(n + m)
        #TC: O(n + m)