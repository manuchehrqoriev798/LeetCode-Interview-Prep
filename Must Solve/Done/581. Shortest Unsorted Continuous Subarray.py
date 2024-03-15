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
        elif end - start + 1 > 1:
            return end - start + 1 
        else:
            return 0




class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)  
        start, end = len(nums), 0  

        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
            
        if end - start + 1 > 0:
            return end - start + 1 
        else:
            return 0