class Solution:
    def addSpaces(self, s, spaces):
        res = []
        r = 0

        # for i,n in enumerate(nums)
        for l, char in enumerate(s):
            if r < len(spaces) and l == spaces[r]:
                res.append(" ")
                r += 1
            res.append(char)
        return "".join(res)
