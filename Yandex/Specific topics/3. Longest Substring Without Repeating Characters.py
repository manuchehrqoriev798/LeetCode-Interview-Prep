class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_index_map = [-1] * 128  
        
        for right in range(len(s)):
            index = ord(s[right])  
            
            if char_index_map[index] >= left:
                left = char_index_map[index] + 1

            char_index_map[index] = right
            max_length = max(max_length, right - left + 1)

        return max_length





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashset = set()
        maxLength = 0
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                r += 1
                maxLength = max(maxLength, r - l)
            else:
                hashset.remove(s[l])
                l += 1
        
        return maxLength



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
            







class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = 0
        hashmap = {}

        l, r = 0, 0

        while r < len(s):
            if s[r] not in hashmap or hashmap[s[r]] < l:
                count = max(count, r - l + 1)
            else:
                l = hashmap[s[r]] + 1

            hashmap[s[r]] = r

            r += 1

        return count




# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         count = 0

#         l, r = 0, 0
#         q = deque()

#         while r < len(s):
#             if s[r] not in q:
#                 q.append(s[r])
#                 r += 1
#                 count = max(count, r - l)
#             else:
#                 q.popleft()
#                 l += 1
        
#         return count



# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         count = 0

#         l, r = 0, 0
#         res = []

#         while r < len(s):
#             if s[r] not in res:
#                 res.append(s[r])
#                 r += 1
#                 count = max(count, r - l)
#             else:
#                 res.remove(s[l])
#                 l += 1
        
#         return count




