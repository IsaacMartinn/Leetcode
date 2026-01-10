from sortedcontainers import SortedDict

class Solution:
    def sortPeople(self, names, heights):
        sorted_dict = SortedDict()
        output = []

        for name, height in zip(names,heights):
            sorted_dict[height] = name
        
        for key, value in sorted_dict.items():
            output.append(value)

        return output[::-1]
    
    #TC is O(Nlogn) could be better
