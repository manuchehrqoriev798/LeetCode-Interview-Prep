class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 2
            else:
                return 1
   
        res = 0
        count = 1 
        
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        
        return max(res, count)





class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        pre = float('-inf')
        l,r = 0,0
        res = 1
        while r < len(nums):
            if nums[r] > pre:
                res = max(r-l+1,res) 
            else:
                l = r
            pre = nums[r]
            r += 1
        return res

