class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  
        
        l = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        
        return l + 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  

        k = 1 
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[k] = nums[r]
                k += 1
        return k