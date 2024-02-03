class Solution:
    def isMonotonic(self, nums:list[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                decreasing = False
            elif nums[i-1] < nums[i]:
                increasing = False
        
        return increasing or decreasing



class Solution:
    def isMonotonic(self, nums:list[int]) -> bool:
        copy_nums = nums.copy()
        nums.sort()
        if copy_nums == nums:
            return True
        elif copy_nums[::-1] == nums:
            return True
        return False