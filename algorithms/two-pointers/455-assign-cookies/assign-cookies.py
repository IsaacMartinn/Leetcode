class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()

        i = j = 0
        count = 0 

        while j < len(s):
            if i < len(g) and s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count
        