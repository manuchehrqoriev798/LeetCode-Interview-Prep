class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        char_set = set()

        res = 0

        for r in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        
        return res






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
    
    
    
    


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        res = ""
        
        while right < len(s) and left <= right:
            if s[right] not in res:
                res += s[right]
                right += 1
                ans = max(ans, len(res))
            else:
                # Remove characters from the left of the substring until the repeated character is removed
                while s[right] in res:
                    res = res[1:]
                    left += 1
                res += s[right]
                right += 1
        
        return ans





