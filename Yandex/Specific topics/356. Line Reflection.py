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
    
    minValue = float("inf")
    maxValue = float("-inf")
    
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

# Example 1
nums1 = [(1, 1), (2, 1), (4, 1), (5, 1)]
print(isReflected(nums1))  









def isReflected(nums):
    if not nums:
        return False
    
    minValue = float("inf")
    maxValue = float("-inf")
    
    seen = {}
    
    for x, y in nums:
        minValue = min(minValue, x)
        maxValue = max(maxValue, x)
        if (x, y) in seen:
            seen[(x, y)] += 1
        else:
            seen[(x, y)] = 1
    
    total = minValue + maxValue
    
    for x, y in nums:
        if (total - x, y) not in seen or seen[(total - x, y)] == 0:
            return False
        seen[(total - x, y)] -= 1
    
    return True

# Example 1
nums1 = [(1, 1), (1, 1), (1, 1), (4, 1), (4, 1)]
print(isReflected(nums1))  # Output: True






