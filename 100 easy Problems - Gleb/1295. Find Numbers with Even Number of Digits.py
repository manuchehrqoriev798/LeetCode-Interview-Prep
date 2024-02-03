class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res = res + 1
        return res



class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def digit_number(num):
            count = 1
            while num > 9:
                num = num // 10
                count += 1
            return count
        
        res = 0
        for num in nums:
            if digit_number(num) % 2 == 0:
                res += 1
        
        return res
