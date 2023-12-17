class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else: 
            return 2 * n

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res = n * (n % 2 +1)
        return res

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * (n % 2 +1)