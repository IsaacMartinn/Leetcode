class Solution:
    def intersection(self, nums1, nums2):
        # output = set()
        # for num in nums1:
        #     if num in nums2:
        #         output.add(num)

        # return list(output)

        seen = set(nums1)
        res = []

        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res
    
