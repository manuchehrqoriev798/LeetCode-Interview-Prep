class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}

        for idx, char in enumerate(s):
            hashmap[char] = idx
        

        mx, count = 0, 0
        res = []

        for idx, char in enumerate(s):
            count += 1

            mx = max(mx, hashmap[char])

            if idx == mx:
                res.append(count)
                count = 0
        
        return res



# # if instead of length it asks for indexes:
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         hashmap = {}

#         for idx, char in enumerate(s):
#             hashmap[char] = idx
        

#         mx, count = 0, 0
#         res = []

#         l, r = 0, 0
#         for idx, char in enumerate(s):
#             count += 1

#             mx = max(mx, hashmap[char])

            
#             if idx == mx:
#                 res.append([l, r])
#                 r += 1
#                 l = r
#                 count = 0
#                 continue

#             r += 1
            
        
#         return res