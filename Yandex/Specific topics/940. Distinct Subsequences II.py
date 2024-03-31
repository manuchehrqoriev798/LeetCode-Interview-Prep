class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # get unstanding for the bottom-up dp next time

        # Top-down DP: O(N) O(N)
        @cache
        def dp(i):
            if i == len(s):
                return 0
            
            seen = set()
            res = 0
            for i in range(i, len(s)):
                if s[i] in seen:
                    continue
                seen.add(s[i])
                res += dp(i+1) + 1
            return res%mod

        mod = int(1e9+7)
        return dp(0)




        # # backtrack subset => TLE
        # def backtrack(start, end, arr):
        #     res.add("".join(arr))
  
            
        #     for i in range(start, end):
        #         arr.append(s[i])
        #         backtrack(i+1, end, arr)
        #         arr.pop()

        # res = set()
        # backtrack(0, len(s), [])
        # print(res)
        # return len(res) -1 







class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        last_occurrence = [-1] * 26
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i-1]) % mod
            if last_occurrence[ord(s[i-1]) - ord('a')] != -1:
                dp[i] -= dp[last_occurrence[ord(s[i-1]) - ord('a')]-1]
            dp[i] %= mod
            last_occurrence[ord(s[i-1]) - ord('a')] = i

        return (dp[n] - 1) % mod