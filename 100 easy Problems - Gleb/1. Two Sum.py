class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            comp = target - num 

            if comp in hashmap:
                return [i, hashmap[comp]]
            
            hashmap[num] = i
        
        return []