356. Line Reflection
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

Input: [[1,1],[-1,1]]
Output: true
Example 2:

Input: [[1,1],[-1,-1]]
Output: false



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










def isReflected(nums):
    if not nums:
        return False
    
    minValue = float("-inf")
    maxValue = float("inf")
    
    seen = set()
    
    
    for x, y in nums:
        minValue = min(minValue, x)
        maxValue = max(maxValue, x)
        seen.add((x, y))
    
    total = minValue + maxValue
    
    for x, y in nums:
        if (total - x, y) not in seen:
            return False
    
    
    return True


isReflected(nums)







