class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            l, r = 0, len(res)
            while l < r:
                mid = (l + r) // 2
                if res[mid] < num:
                    l = mid + 1
                else:
                    r = mid

            if r >= len(res):
                res.append(num)
            else:
                res[r] = num
                
        return len(res)