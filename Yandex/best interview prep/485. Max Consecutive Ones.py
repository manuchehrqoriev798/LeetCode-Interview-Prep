class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        l, r = 0, 0

        while r < len(nums):
            while r < len(nums) and nums[r] == 1:
                r += 1
            
            maxCount = max(maxCount, r - l)

            r += 1
            l = r
        
        return maxCount



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        
        return max(maxCount, count)