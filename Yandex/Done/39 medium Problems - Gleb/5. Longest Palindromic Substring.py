class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def palindrome(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        res = ""
        for i in range(n):
            p1 = palindrome(i, i)
            p2 = palindrome(i, i + 1)
            
            if len(res) >= len(p1):
                res = res
            else:
                res = p1
            
            if len(res) >= len(p2):
                res = res
            else:
                res = p2

        return res