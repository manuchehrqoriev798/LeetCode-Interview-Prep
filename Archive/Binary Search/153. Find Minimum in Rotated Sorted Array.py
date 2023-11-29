class Solution:
    def findMin(self, nums: List[int]) -> int:

        new_nums = sorted(nums)
        return (new_nums[0])


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        # Perform a binary search until the left pointer is less than or equal to the right pointer
        while l <= r:
            # If the array is already sorted, update res with the minimum of the current element and res
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res
                
            m = (l + r) // 2

            res = min(res, nums[m])

            # Adjust pointers based on the comparison of middle and left elements
            if nums[m] >= nums[l]:
                # If the middle element is greater than or equal to the left element, move the left pointer to the right of the middle
                l = m + 1 
            else:
                # If the middle element is less than the left element, move the right pointer to the left of the middle
                r = m - 1
        
        return res


class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2  
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
    