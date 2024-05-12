class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l, r = 0, 1
        increasing = True
        decreasing = True

        while r < len(nums):
            if nums[l] < nums[r]:
                decreasing = False
            elif nums[l] > nums[r]:
                increasing = False
            l += 1
            r += 1
        
        return increasing or decreasing



class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        
        l, r = 0, 1

        while r < len(nums):
            if nums[l] <= nums[r]:
                l += 1
                r += 1
            else:
                break
        
        if r == len(nums):
            return True
        
        l, r = 0, 1
        while r < len(nums):
            if nums[l] >= nums[r]:
                l += 1
                r += 1
            else:
                break
        
        if r == len(nums):
            return True
        
        return False




class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        
        r = 0
        while r < len(nums):
            if r + 1 < len(nums) and nums[r] <= nums[r + 1]:
                r += 1
            else:
                break
        
        if r + 1 == len(nums):
            return True
        
        r = 0
        while r < len(nums):
            if r + 1 < len(nums) and nums[r] >= nums[r + 1]:
                r += 1
            else:
                break
        
        if r + 1== len(nums):
            return True
        
        return False