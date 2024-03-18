class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r = 0, 0

        res = []
        while r < len(nums):
            while r + 1 < len(nums) and nums[r + 1] - nums[r] == 1:
                r += 1
            
            if l == r:
                res.append(f"{nums[l]}")
            else:
                res.append(f"{nums[l]}->{nums[r]}")
            
            r += 1
            l = r
        
        return res



class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r = 0, 1

        res = []
        while l < len(nums):
            while r < len(nums) and nums[r] - nums[r - 1] == 1:
                r += 1
            
            if r - l == 1:
                res.append(f"{nums[l]}")
            else:
                res.append(f"{nums[l]}->{nums[r - 1]}")
            
            l = r
            r += 1
        
        return res