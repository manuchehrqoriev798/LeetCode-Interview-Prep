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





class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        return sorted(nums)