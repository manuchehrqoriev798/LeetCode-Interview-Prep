class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0
            nStr = str(n)
            for i in range(len(nStr)):
                total += int(nStr[i]) ** 2

            n = total

        return n == 1



class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n = n // 10

            n = total

        return n == 1