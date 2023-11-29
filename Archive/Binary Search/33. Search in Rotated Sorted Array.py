class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r+l)//2
            if target == nums[m]:
                return m

            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: 
                    r = m - 1

            # right sorted portion
            else: 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l = 0 
        r = n - 1 

        while l <= r:
            m = (l+r)//2
            

            if nums[m] >= nums[l]: #m is in left sorted portion:

                if target > nums[m]:
                    l = m + 1 

                elif target < nums[m]:
                    if target >= nums[l]:
                        r = m - 1 
                    else:
                        l = m + 1
                else:
                    return m 
            
            else: #m is in right sorted portion
                if target > nums[m]:
                    if target > nums[r]:
                        r = m - 1 
                    else:
                        l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    return m
        
        return -1




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m

            #in left sorted array
            if nums[m] >= nums[l]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            
            #right sorted array
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1



