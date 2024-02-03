class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n > 1:
            if n % 4 != 0:
                return False
            else:
                n = n / 4
        
        return True



class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 4 == 0:
            return self.isPowerOfFour(n // 4)
        else:
            return False



class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        return self.isPowerOfFour(n / 4)