class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(1, n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        numbers = list(range(1, n + 1)) 
        num1 = sum(filter(lambda x: x % m != 0, numbers))  
        num2 = sum(filter(lambda x: x % m == 0, numbers))  
        return num1 - num2
