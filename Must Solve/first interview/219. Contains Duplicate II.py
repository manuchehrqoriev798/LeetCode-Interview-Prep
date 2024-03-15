class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap and abs(i - hashmap[nums[i]] <= k):
                return True
            hashmap[nums[i]] = i
        
        return False





class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i, n in enumerate(nums):
          if n in hashmap and abs(i - hashmap[n]) <= k:
            return True
          else:
            hashmap[n] = i
        
        return False