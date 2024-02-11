class Solution:
    def maxConsequtiveOnes2(self, nums: List[int]) -> int:
        l, r = 0, 0
        zeros = 0
        max_length = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

            r += 1
        
        return max_length