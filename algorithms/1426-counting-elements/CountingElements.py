class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for x in arr:
            if x + 1 in hash_set:
                count += 1
        return count

        #T.C: O(N)
        #S.C: O(N)
