class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        res = ""
        ans = 0
        while j<n and i<=j:
            if s[j] not in res:
                res += s[j]
                j += 1
                ans = max(ans , len(res))

            else:
                while s[j] in res:
                    
                    res = res[1:]
                    i+=1
                # ans = max(ans , len(res))
                res += s[j]
                j += 1
        return ans






class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        char = set()
        res = 0
        
        while r < len(s):
            while (s[r] in char):
                char.remove(s[l])
                l += 1
            char.add(s[r])
            res = max(res,r-l+1)
            r += 1
        
        return res
