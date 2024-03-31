class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)



class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            T0, T1, T2 = 0, 1, 1
            for i in range(3, n + 1):
                Tn = T0 + T1 + T2
                T0, T1, T2 = T1, T2, Tn

            return T2