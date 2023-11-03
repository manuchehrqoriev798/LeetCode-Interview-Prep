# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         l = 0
#         r = 0
#         arrayS1 = []
#         for letter in s1:
#             arrayS1.append(letter)

#         while r < len(s2):
#             if s2[r] in arrayS1:
#                 arrayS1.remove(s2[r])
#                 r += 1
#             else:
#                 arrayS1.append(s2[l])
#                 l += 1

#             if not arrayS1:
#                 return True

#         return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            s2Count[ord(s2[r]) - ord('a')] += 1
            if s2Count[ord(s2[r]) - ord('a')] == s1Count[ord(s2[r]) - ord('a')]:
                matches += 1
            elif s2Count[ord(s2[r]) - ord('a')] == s1Count[ord(s2[r]) - ord('a')] + 1:
                matches -= 1
            s2Count[ord(s2[l]) - ord('a')] -= 1
            if s2Count[ord(s2[l]) - ord('a')] == s1Count[ord(s2[l]) - ord('a')]:
                matches += 1
            elif s2Count[ord(s2[l]) - ord('a')] == s1Count[ord(s2[l]) - ord('a')] - 1:
                matches -= 1
            l += 1
        return matches == 26
        




# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         s1Count, s2Count = [0] * 26, [0] * 26

#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord('a')] += 1
#             s2Count[ord(s2[i]) - ord('a')] += 1

#         for i in range(len(s1), len(s2)):
#             if s1Count == s2Count:
#                 return True

#             s2Count[ord(s2[i]) - ord('a')] += 1
#             s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1

#         return s1Count == s2Count

