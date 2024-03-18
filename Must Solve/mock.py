def maxSubarray(nums):
    maximum = float("-inf")
    for num in nums:
        maximum = max(maximum, num)
        
    total = 0
    for num in nums:
        total += num
        
        maximum = max(maximum, total)
        
        if total < 0:
            total = 0
    
    return maximum
