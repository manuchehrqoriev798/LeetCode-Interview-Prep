# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         lowercase_s = s.lower()
#         text = ''
#         for letter in lowercase_s:
#             if letter.isalnum():
#                 text += letter
#         if text == text[::-1]:
#             return True
#         else: 
#             return False



# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         lowercase_s = s.lower()
#         text = ''
#         for letter in lowercase_s:
#             if letter.isalnum():
#                 text += letter
#         l = 0
#         r = -1
#         for i in range(len(text)-1):
#             if text[l] == text[r]:
#                 l += 1
#                 r -= 1
#             else: 
#                 return False
#         return True



class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        return (
            'A' <= c <= 'Z' or 
            'a' <= c <= 'z' or 
            '0' <= c <= '9'
        )