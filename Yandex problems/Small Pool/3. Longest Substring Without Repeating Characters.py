class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        d = {}

        max_length = 0

        while r < len(s):
            if s[r] not in d or d[s[r]] == 0:
                d[s[r]] = 1
                r += 1
                max_length = max(max_length, r - l)
            else:
                d[s[l]] -= 1
                l += 1
            
        
        return max_length




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        q = deque()
        max_length = 0

        while r < len(s):
            if s[r] not in q:
                q.append(s[r])
                r += 1
                max_length = max(max_length, r - l)
            else:
                q.popleft()
                l += 1
        
        return max_length