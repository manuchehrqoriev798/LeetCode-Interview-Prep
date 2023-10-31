class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <=r:
            # m = (l+r)//2 # there might be an overflow while adding
            m = l + ((r-l)//2)
            if nums[m]>target:
                r = m -1 # shifts the r into m - l 
            elif nums[m]< target:
                l = m + 1
            else:
                return m
        return -1

