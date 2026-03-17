class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1] == c.lower() and ord(c) < 97:
                stack.pop()
            elif stack and stack[-1] == c.upper() and ord(c) >= 97:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
        