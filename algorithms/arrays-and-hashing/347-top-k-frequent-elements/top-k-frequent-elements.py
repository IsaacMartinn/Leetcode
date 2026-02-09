from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1 
        
        freq_list = []
        for key, value in freq.items():
            freq_list.append([value, key])
        
        freq_list.sort(reverse=True)

        output = []
        for i in range(k):
            output.append(freq_list[i][1])
        
        return output

        #TC: O(nlogn)
        #SC: O(n)
