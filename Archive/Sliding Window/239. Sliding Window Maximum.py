






















# Does not pass the time limit
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        l = 0

        res = []

        for r in range(0, len(nums) - k + 1):
            maximum = max(nums[l:(r + k)])
            res.append(maximum)
            l += 1
        
        return res