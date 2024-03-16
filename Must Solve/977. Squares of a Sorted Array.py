class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(res) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) <= abs(nums[r]):
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
        
        return res




class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums) 
        index = r

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[index] = nums[r] ** 2  
                r -= 1
            else:
                res[index] = nums[l] ** 2
                l += 1
            
            index -= 1
        
        return res