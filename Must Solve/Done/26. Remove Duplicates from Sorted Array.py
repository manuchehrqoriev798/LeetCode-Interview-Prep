class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
            
            r += 1

        return l + 1



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  
        
        count = 1

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                count += 1
            else:
                nums[i - 1] = "_"
        
        l, r = 0, 1
        while l < r and r < len(nums):
            if nums[l] == "_" and nums[r] != "_":
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            if nums[l] != "_":
                l += 1
            r += 1
            
        return count