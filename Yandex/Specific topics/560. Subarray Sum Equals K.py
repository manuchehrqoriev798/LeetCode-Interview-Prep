class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        total = 0

        for num in nums:
            total += num

            if (total - k) in hashmap:
                count += hashmap[total - k]
            
            if total not in hashmap:
                hashmap[total] = 1
            else:
                hashmap[total] += 1
        
        return count