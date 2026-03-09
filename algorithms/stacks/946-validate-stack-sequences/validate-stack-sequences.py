class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        i = 0 
        stack = []

        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        if len(stack) == 0:
            return True
        return False