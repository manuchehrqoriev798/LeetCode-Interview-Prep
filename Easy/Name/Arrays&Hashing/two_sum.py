from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Example usage
solution = Solution()
nums = [2, 9, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)
