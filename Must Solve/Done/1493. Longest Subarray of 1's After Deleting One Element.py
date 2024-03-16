class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        count = 0
        l, r = 0, 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            count = max(count, r - l + 1 - zeros)

            r += 1
        
        if count == len(nums):
            return count - 1
        else:
            return count