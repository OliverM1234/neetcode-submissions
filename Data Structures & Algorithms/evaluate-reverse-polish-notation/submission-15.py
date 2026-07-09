class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:
            try:
                stack.append(int(t))
            except ValueError:
                y = stack.pop()
                x = stack.pop()
                if t == "+":
                    stack.append(x+y)
                elif t == "-":
                    stack.append(x-y)
                elif t == "*":
                    stack.append(x*y)
                elif t == "/":
                    stack.append(int(x / y))
        return stack.pop()
                    