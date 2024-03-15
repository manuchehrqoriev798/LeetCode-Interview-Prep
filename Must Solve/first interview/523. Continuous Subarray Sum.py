class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        hashmap = {0:-1}
        
        total = 0
        for index, num in enumerate(nums):
            total = total + num
            reminder = total % k

            if reminder not in hashmap:
                hashmap[reminder] = index
            elif index - hashmap[reminder] > 1:
                return True

        return False