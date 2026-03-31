class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        l, curr_white = 0, 0

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                curr_white += 1
            if r - l + 1 >= k:
                res = min(curr_white, res)
                if blocks[l] == 'W':
                    curr_white -= 1
                l += 1
        return res
