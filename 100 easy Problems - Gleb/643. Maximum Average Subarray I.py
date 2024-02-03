class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur  = sum(nums[:k])
        res = cur

        for i in range(k, len(nums)):
            cur = cur - nums[i - k]
            cur = cur + nums[i]

            res = max(res, cur)
        
        return res / k





class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')  

        count = 0
        cur = 0

        for i in range(len(nums)):
            cur += nums[i]
            count += 1
            
            if count == k:
                res = max(res, cur)
            
            if count > k:
                cur -= nums[i - k]
                res = max(res, cur)
            
        
        return res / k