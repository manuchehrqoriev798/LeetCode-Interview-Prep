class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
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
