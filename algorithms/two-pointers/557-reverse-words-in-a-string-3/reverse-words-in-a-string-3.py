class Solution:
    def reverseWords(self, s: str) -> str:
        new_string = s.split()
        
        for i, word in enumerate(new_string):
            char_list = list(word)

            l, r = 0, len(char_list) - 1
            while l < r: 
                char_list[l], char_list[r] = char_list[r], char_list[l]
                l += 1 
                r -= 1
            new_string[i] = "".join(char_list)
        return " ".join(new_string)

        #TC: O(n)
            