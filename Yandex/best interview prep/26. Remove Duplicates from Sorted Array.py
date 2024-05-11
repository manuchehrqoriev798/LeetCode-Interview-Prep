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
        l, r = 0, 1

        while r < len(nums):
            if nums[l] == nums[r]:
                nums[l] = "_"
                l = r
                r += 1
            else:
                l += 1
                r += 1

                
        l, r = 0, 0
        while r < len(nums):
            if nums[l] == "_" and nums[r] != "_":
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[l] != "_":
                l += 1
            r += 1

        return l