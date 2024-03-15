class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            newN = 0
            nStr = str(n)
            for i in range(len(nStr)):
                newN += int(nStr[i]) ** 2
            n = newN
            newN = 0
            

        return n == 1



class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            newN = 0
            while n > 0:
                reminder = n % 10
                n = n // 10
                newN += reminder ** 2
            n = newN
            newN = 0

        return n == 1

