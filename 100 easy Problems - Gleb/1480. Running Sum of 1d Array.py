class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums




class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0

        for i in range(len(nums)):
            count += nums[i] 
            nums[i] = count
        
        return nums