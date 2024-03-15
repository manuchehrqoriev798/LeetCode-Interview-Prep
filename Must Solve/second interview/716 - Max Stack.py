class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self) -> int:
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_val = self.max_stack.pop()
        buffer = []
        while self.stack[-1] != max_val:
            buffer.append(self.stack.pop())
        self.stack.pop()
        while buffer:
            self.push(buffer.pop())
        return max_val
