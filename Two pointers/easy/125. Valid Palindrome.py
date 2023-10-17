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
