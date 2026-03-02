class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if stack and s[i] == "D" and stack[-1] == "C":
                    stack.pop()
            elif stack and s[i] == "B" and stack[-1] == "A":
                    stack.pop()
            else:
                stack.append(s[i])
        return len(stack)