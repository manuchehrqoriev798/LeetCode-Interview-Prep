class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            t1, t2 = 0, 1
            for i in range(2, n + 1):
                tn = t1 + t2
                t1, t2 = t2, tn
            return t2


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n - 2) + self.fib(n - 1)