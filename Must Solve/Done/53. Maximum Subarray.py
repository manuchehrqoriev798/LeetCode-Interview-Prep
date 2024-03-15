class Solution(object):
    def maxSubArray(self, nums):
        maxSum = float("-inf")
        cur = 0

        for num in nums:
            cur += num

            if cur > maxSum:
                maxSum = cur
            
            if cur < 0:
                cur = 0
        
        return maxSum