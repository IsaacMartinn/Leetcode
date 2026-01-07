class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        output = []

        for i,n in enumerate(nums):
            if n not in hash:
                hash[n] = [i]
            else:
                hash[n].append(i)
        
        for key, values in hash.items():
            if len(values)> 1:
                # output.append(len(values))
                
                for i in range(len(values)):
                    index = i + 1
                    output.append(len(values) - index) 
        
        return sum(output)
