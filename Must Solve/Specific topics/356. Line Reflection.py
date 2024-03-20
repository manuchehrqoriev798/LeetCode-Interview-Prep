# 356. Line Reflection
# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

# Example 1:

# Input: [[1,1],[-1,1]]
# Output: true
# Example 2:

# Input: [[1,1],[-1,-1]]
# Output: false




nums =  [[1,1],[-1,-1]]
def isReflected(nums):
    if not nums:
        return False
    
    nums_set = set()
    for point in nums:
        nums_set.add(tuple(point))

    
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if (-1 * nums[i][0], nums[i][1]) not in nums_set:
                return False
    
    return True


isReflected(nums)

# class Solution:
#     def isReflected(self, points: List[List[int]]) -> bool:
#         min_x, max_x = inf, -inf
#         point_set = set()
#         for x, y in points:
#             min_x = min(min_x, x)
#             max_x = max(max_x, x)
#             point_set.add((x, y))
#         s = min_x + max_x
#         return all((s - x, y) in point_set for x, y in points)