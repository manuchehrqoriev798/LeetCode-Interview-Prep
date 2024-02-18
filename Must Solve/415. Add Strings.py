class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l, r = len(num1) - 1, len(num2) - 1

        res = [0] * max(len(num1), len(num2))

        carry = 0

        for i in range(len(res) - 1, -1, -1):
            digit = carry
            if l >= 0:
                digit += int(num1[l])
                l -= 1
            if r >= 0:
                digit += int(num2[r])
                r -= 1

            carry = digit // 10
            res[i] = str(digit % 10)

        if carry > 0:
            res = [str(carry)] + res

        return "".join(res)
