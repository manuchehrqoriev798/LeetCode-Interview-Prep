from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        maxCount = 0
        zeros = 0
        
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            
            while zeros == 2:
                if nums[l] == 0:
                    zeros = 1
                l += 1
            
            maxCount = max(maxCount, r - l + 1)
            
            r += 1
        
        return maxCount


solution = Solution()

nums = [1, 0, 1, 0, 1, 1, 0, 0]


print(solution.findMaxConsecutiveOnes(nums))