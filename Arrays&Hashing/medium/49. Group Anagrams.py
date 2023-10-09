# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_map = {}
#         result = []

#         for i in strs:
#             sorted_i = ''.join(sorted(i))
            
#             if sorted_i not in anagram_map:
#                 anagram_map[sorted_i] = []
#             anagram_map[sorted_i].append(i)

#         result = list(anagram_map.values())
#         return result

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]





from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())

# Sample input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Create an instance of the Solution class
solution = Solution()

# Call the groupAnagrams function with the provided input
result = solution.groupAnagrams(strs)

# Print the result
print(result)
