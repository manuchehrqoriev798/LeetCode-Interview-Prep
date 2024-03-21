class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0

        while r < len(nums):
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[l] != val:
                l += 1

            r += 1

        return l 


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0

        while r < len(nums):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            
            r += 1
        
        return l 





class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 1

        while r < len(nums):
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[l] != val:
                l += 1

            r += 1
        
        if l < len(nums) and nums[l] == val:
            return l
        else:
            return l + 1