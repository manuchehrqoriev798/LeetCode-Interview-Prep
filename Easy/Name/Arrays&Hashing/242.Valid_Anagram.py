# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         char_count_s = {}
#         char_count_t = {}
        
#         for char in s:
#             char_count_s[char] = char_count_s.get(char, 0) + 1
        
#         for char in t:
#             char_count_t[char] = char_count_t.get(char, 0) + 1
        
#         return char_count_s == char_count_t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else: 
            return False



            
# Create an instance of the Solution class
solution = Solution()

# Test case 1: Two strings that are anagrams
s1 = "listen"
t1 = "silent"
result1 = solution.isAnagram(s1, t1)
print(f"Test case 1: s1 = {s1}, t1 = {t1}")
print("Result:", result1)  # Expected output: True

# Test case 2: Two strings that are not anagrams
s2 = "hello"
t2 = "world"
result2 = solution.isAnagram(s2, t2)
print(f"\nTest case 2: s2 = {s2}, t2 = {t2}")
print("Result:", result2)  # Expected output: False
