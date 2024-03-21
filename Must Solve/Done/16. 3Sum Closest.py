class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float("inf")

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(target - total) < abs(target - closest):
                    closest = total


                if total < target:
                    l += 1
                else:
                    r -= 1
        
        return closest