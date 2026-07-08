class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        if not self.mins:
            self.stack.append(val)
            self.mins.append(val)
        else:
            self.stack.append(val)
            self.mins.append(min(self.mins[-1],val))




    def pop(self) -> None:
        self.mins.pop()
        return self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.mins[-1] == -3:
            print(self.stack)
            print(self.mins)
        return self.mins[-1]
