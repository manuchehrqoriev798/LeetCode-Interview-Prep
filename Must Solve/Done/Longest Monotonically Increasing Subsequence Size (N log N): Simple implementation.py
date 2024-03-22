def longest_monotic_increasing_subsequence(nums):
    r = 0
    maxCount = 0
    while r < len(nums):
        count = 1
        while r + 1 < len(nums) and nums[r] < nums[r + 1]:
            r += 1
            count += 1
        maxCount = max(maxCount, count)
        r += 1
    return maxCount

arr = [8, 9, 12, 10, 11]
print(longest_monotic_increasing_subsequence(arr))



def longest_monotonic_increasing_subsequence(nums):
    if not nums:
        return 0
    
    maxCount = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 1

    return max(maxCount, count)

arr = [8, 9, 12, 10, 11]
print(longest_monotonic_increasing_subsequence(arr))
