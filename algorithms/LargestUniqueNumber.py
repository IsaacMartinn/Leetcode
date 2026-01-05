class Solution:
    def largestUniqueNumber(self, nums) -> int:

        hash = {}
        output = -1

        for i, n in enumerate(nums):
            if n not in hash:
                hash[n] = 1
            else:
                hash[n] += 1

        for key, value in hash.items():
            if hash[key] == 1:
                if key > output:
                    output = key

        return output
