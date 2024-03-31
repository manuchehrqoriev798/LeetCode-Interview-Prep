class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(start, end, score):
            if end - start + 1 < 2:
                return 0
            ans = 0
            if nums[start] + nums[start + 1] == score:
                ans = max(ans, 1 + dfs(start + 2, end, score))
            if nums[end - 1] + nums[end] == score:
                ans = max(ans, 1 + dfs(start, end - 2, score))
            if nums[start] + nums[end] == score:
                ans = max(ans, 1 + dfs(start + 1, end - 1, score))
            return ans
        n = len(nums)
        return max(dfs(0, n - 1, nums[0] + nums[1]), dfs(0, n - 1, nums[-1] + nums[-2]), dfs(0, n - 1, nums[0] + nums[-1]))