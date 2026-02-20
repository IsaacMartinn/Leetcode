class Solution:
    def calPoints(self, operations) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif operations[i] == "D":
                stack.append(int(stack[-1]) * 2)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))
        
        return sum(stack)
        