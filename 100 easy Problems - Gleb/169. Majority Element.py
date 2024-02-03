class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)/2]



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        n = len(nums) // 2
        for key, value in hashmap.items():
            if value > n:
                return key
        
        return 0



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]