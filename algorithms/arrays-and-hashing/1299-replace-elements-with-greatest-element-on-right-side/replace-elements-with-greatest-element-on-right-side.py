class Solution:
    def replaceElements(self, arr):
        n = len(arr) 
        res = [0] * n 
        right_max = -1

        #start at the last index, end at the first, stepping backwards by 1
        for i in range(n - 1, -1, -1):
            res[i] = right_max
            right_max = max(right_max, arr[i])
        return res

        #TC: O(n)