class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_a = []
        stack_b = []

        for char in s:
            if char == "#" and len(stack_a) > 0:
                stack_a.pop()
            elif char == "#" and len(stack_a) == 0:
                continue
            else:
                stack_a.append(char)

        for char in t:
            if char == "#" and len(stack_b) > 0:
                stack_b.pop()
            elif char == "#" and len(stack_b) == 0:
                continue
            else:
                stack_b.append(char)
        return "".join(stack_a) == "".join(stack_b)
     