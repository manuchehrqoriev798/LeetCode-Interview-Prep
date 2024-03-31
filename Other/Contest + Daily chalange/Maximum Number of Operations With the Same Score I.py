class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count = 0
        l, r = 0, 1
        target = nums[l] + nums[r]
        while r < len(nums):
            another = nums[l] + nums[r]

            if another != target:
                return count

            count += 1

            l += 2
            r += 2
            target = another
        return count
