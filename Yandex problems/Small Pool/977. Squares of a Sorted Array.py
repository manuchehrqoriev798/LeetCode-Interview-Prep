class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        l, r, index = 0, n - 1, n - 1
        
        while l <= r:
            l_sqr = nums[l] ** 2
            r_sqr = nums[r] ** 2
            
            if l_sqr >= r_sqr:
                result[index] = l_sqr
                l += 1
            else:
                result[index] = r_sqr
                r -= 1
            
            index -= 1
        
        return result




class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        return sorted(nums)