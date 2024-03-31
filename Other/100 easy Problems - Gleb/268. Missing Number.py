class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums)):
            if nums[i] != count:
                return count
            count += 1
        
        return count


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = {}
        
        for num in nums:
            hashmap[num] = 1
        
        for miss in range(len(nums) + 1):
            if miss not in hashmap:
                return miss