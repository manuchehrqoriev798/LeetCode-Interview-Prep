class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        d = {0:-1}
        
        total = 0

        for index, num in enumerate(nums):
            total += num
            reminder = total % k

            if reminder in d:
                if abs(index - d[reminder]) >= 2:
                    return True
            else:
                d[reminder] = index
        
        return False
            