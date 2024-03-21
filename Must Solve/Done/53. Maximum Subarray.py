class Solution(object):
    def maxSubArray(self, nums):
        maxSum = float("-inf")
        
        total = 0
        for num in nums:
            total += num

            if total > maxSum:
                maxSum = total
            
            if total < 0:
                total = 0
        
        return maxSum







class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minimum = min(nums)

        maximum = minimum
        total = 0

        for num in nums:
            total += num
            
            maximum = max(maximum, total)
        
            if total < 0:
                total = 0
        return maximum