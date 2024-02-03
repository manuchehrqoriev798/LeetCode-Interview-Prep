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




class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}

        for i, n in enumerate(nums):
            if n not in h:
                h[n] = [i]
            else:
                h[n].append(i)

        for i, n in enumerate(nums):
            for j in h[n]:
                if i < j and j - i <= k:
                    return True
        
        return False