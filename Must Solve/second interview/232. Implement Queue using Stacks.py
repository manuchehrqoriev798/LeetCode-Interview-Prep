class MyQueue:
    def __init__(self):
        self.a, self.b = [], []


    def push(self, x: int) -> None:
        self.a.append(x)
    

    def pop(self) -> int:
        self._move()

        return self.b.pop()
        

    def peek(self) -> int:
        self._move()

        return self.b[-1]
        

    def empty(self) -> bool:
        return not (self.a or self.b)
    

    def _move(self):
        if not self.b:
            for _ in range(len(self.a)):
                self.b.append(self.a.pop())