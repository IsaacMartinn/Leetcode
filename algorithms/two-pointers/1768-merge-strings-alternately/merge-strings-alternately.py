class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = r = 0

        output = ""

        game_on = True

        while game_on:
            if l < len(word1):
                output += word1[l]
                l += 1
            if r < len(word2):
                output += word2[r]
                r += 1
            if l == len(word1) and r == len(word2):
                game_on = False
            
                
        return output

        #TC: O(n + m)
        #SC: O (n + m)
