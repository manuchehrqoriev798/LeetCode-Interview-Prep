class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
    
        # Find the first element out of order from the left
        while left < right and nums[left] <= nums[left + 1]:
            left += 1
    
        # Array is already sorted
        if left == n - 1:
            return 0
    
        # Find the first element out of order from the right
        while left < right and nums[right] >= nums[right - 1]:
            right -= 1
    
        # Find the minimum and maximum values within the unsorted subarray
        subarray_min = min(nums[left:right + 1])
        subarray_max = max(nums[left:right + 1])
    
        # Extend the subarray to include elements greater than subarray_min
        while left >= 0 and nums[left] > subarray_min:
            left -= 1
    
        # Extend the subarray to include elements smaller than subarray_max
        while right < n and nums[right] < subarray_max:
            right += 1
    
        return right - left - 1