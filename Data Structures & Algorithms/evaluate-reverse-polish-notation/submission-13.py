class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:
            print(stack,t)
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
                    if y==0:
                        print(y)
                        continue
                    stack.append(int(x / y))
                else:
                    print("?????????")
                    print(t)
        return stack.pop()
                    