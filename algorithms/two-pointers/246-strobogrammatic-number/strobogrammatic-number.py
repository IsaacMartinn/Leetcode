class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
    
        strob_dict = {
            "0": "0",
            "1": "1",
            "8": "8",
            "6": "9",
            "9":"6"
        }

        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in strob_dict or strob_dict[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True

        