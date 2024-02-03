class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n > 1:
            if n % 2 == 1:
                return False
            else:
                n = n / 2

        return True



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n > 1:
            if n % 2 != 0:
                return False
            else:
                n = n / 2

        return True
    

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        return self.isPowerOfTwo(n / 2)