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




class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            index = bisect.bisect_left(res, n) # Binary search to find where the element would go in a sorted array
            if index >= len(res):
                res.append(n)
            else:
                res[index] = n
        return len(res)




import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                i = bisect.bisect_left(res, n)
                res[i] = n
        return len(res)