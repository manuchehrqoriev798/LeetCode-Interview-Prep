class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        carry=0

        l, r = len(a) - 1, len(b) - 1

        while l >= 0 or r >= 0 or carry:
            if l >= 0:
                carry+=int(a[l])
                l -= 1

            if r >= 0:
                carry+=int(b[r])
                r -= 1

            res.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(res))