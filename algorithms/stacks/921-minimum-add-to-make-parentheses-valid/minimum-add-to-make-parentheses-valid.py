class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close_to_open = {")":"("}
        stack = []

        for c in s:
            if stack and stack[-1] == "(" and c == ")":
                stack.pop()
            else:
                stack.append(c)
            
        return len(stack)
    
    #TC: O(n)
    #SC: O(n)