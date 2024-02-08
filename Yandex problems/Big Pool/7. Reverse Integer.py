class Solution:
    def reverse(self, x: int) -> int:
        if 10 > x >= 0:
            return x

        sign = 1 if x > 0 else -1
        x = abs(x)
        reversed_num = 0

        while x != 0:
            last_digit = x % 10

            reversed_num = reversed_num * 10 + last_digit

            x //= 10
        
        if reversed_num >  2**31 - 1 or -1 * reversed_num < -2**31:
            return 0
        return sign * reversed_num





