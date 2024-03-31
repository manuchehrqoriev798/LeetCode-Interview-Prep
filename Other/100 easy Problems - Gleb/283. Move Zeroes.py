class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return nums
        
        l, r = 0, 0

        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        
        return nums
    
    
    
    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return

        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        
        return nums





    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return

        l, r = 0, 1
        
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[l] != 0:
                l += 1
            
            r += 1
                   
        return nums 

