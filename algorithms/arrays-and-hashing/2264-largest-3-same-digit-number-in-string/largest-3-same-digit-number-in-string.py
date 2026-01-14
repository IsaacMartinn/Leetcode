class Solution:
    def largestGoodInteger(self, num):
        max_total = ""
        current_ord = highest_ord = -1

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                current_ord = ord(num[i])
                highest_ord = max(current_ord,highest_ord)
        
        if highest_ord == -1:
            return ""

        max_total = chr(highest_ord)+chr(highest_ord)+chr(highest_ord)
        return max_total
    