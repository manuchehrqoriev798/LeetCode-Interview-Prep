class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        orig = x
        new = 0
        
        while x > 0:
            reminder = x % 10
            x = x // 10
            new = new * 10 + reminder
        
        return orig == new



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        orig = x
        new = 0
        
        while x > 0:
            x, reminder = divmod(x, 10)
            new = new * 10 + reminder
        
        return orig == new