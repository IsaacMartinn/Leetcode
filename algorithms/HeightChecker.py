class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        res = 0
        
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                res+= 1
        return res
    
    #could be more efficent 
    #Time complexity: O(nlogn) bc of the sorted built in function
    #S.C: O(n)
    #T.C could be O(n)