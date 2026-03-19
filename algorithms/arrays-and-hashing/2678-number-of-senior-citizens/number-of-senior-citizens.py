class Solution:
    def countSeniors(self, details) -> int:
        res = 0 

        for d in details:
            if int(d[11:13]) > 60:
                res += 1
        return res
        