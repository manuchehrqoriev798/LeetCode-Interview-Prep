class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and nums[i] == nums[j]:
                    count += 1
        
        return count




class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    count=count+1
        return count





class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hashmap = {}

        for num in nums:
            if num in hashmap:
                count += hashmap[num]
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        return count