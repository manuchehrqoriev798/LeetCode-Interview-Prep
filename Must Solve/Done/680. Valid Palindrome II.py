class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                string1 = s[:l] + s[l+1:]
                string2 = s[:r] + s[r+1:]
                return string1 == string1[::-1] or string2 == string2[::-1]

            l += 1
            r -= 1
        
        return True