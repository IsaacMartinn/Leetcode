class Solution:
    def anagramMappings(self, nums1, nums2):

        output = []

        for num in nums1:
            output.append(nums2.index(num))
            
        return output
        # TC: O(n^2)
        # SC: O(n)
        #bad need to redo better