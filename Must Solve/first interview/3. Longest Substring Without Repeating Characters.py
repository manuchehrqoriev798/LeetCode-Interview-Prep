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




