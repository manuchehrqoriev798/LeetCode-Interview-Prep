from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_count = [0] * 26
        for char in p:
            p_count[ord(char) - ord('a')] += 1

        s_count = [0] * 26
        indices = []

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if s_count == p_count:
                indices.append(i - len(p) + 1)

        return indices

s = "cbaebabacd"
p = "abc"

solution = Solution()
print(solution.findAnagrams(s, p))










class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        window_count = Counter(s[:len(p)])
        p_count = Counter(p)

        res = []

        for i in range(len(s) - len(p) + 1):  
            if p_count == window_count:
                res.append(i)

            if i + len(p) < len(s): 
                window_count[s[i]] -= 1
                if window_count[s[i]] == 0:
                    del window_count[s[i]]
                window_count[s[i + len(p)]] += 1

        return res

