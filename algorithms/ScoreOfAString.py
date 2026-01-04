class Solution:
    def scoreOfString(self, s: str) -> int:

        char_list = list(s)
        total = 0 
        for i in range(1,len(char_list)):
            total += abs(ord(char_list[i]) - ord(char_list[i-1]))
        return total