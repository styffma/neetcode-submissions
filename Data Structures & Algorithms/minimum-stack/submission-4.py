class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            self.stack.append(val)
            if val <= self.minstack[-1]:
                self.minstack.append(val)
    

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.minstack[-1]:
            self.minstack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
