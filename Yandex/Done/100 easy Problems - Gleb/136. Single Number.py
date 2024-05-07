class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        for key, value in hashmap.items():
            if value == 1:
                return key



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for num, count in counter.items():
            if count == 1:
                return num
