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





class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)  
        start, end = len(nums) - 1, 0  

        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
            
        if end - start + 1 == 1:
            return 0
        elif end - start + 1 > 0:
            return end - start + 1 
        else:
            return 0
    






class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r and nums[l] <= nums[l + 1]:
            l += 1
        
        while l < r and nums[r] >= nums[r - 1]:
            r -= 1
        

        if l == len(nums) - 1:
            return 0


        minimum = min(nums[l:r+1])
        maximum = max(nums[l:r+1])

        while l >= 0 and nums[l] > minimum:
            l -= 1
        
        while r < len(nums) and nums[r] < maximum:
            r += 1
        
        return r - l - 1