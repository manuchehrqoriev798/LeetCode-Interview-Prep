from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an empty dictionary called "anagram_map" to store anagram groups.
        anagram_map = {}
        # Create an empty list called "result" to store the final result.
        result = []

        # Iterate through each string ("i") in the input list "strs."
        for i in strs:
            # Sort the characters in the string "i" and join them back into a string.
            sorted_i = ''.join(sorted(i))
            
            # Check if the sorted string "sorted_i" is not already a key in "anagram_map."
            if sorted_i not in anagram_map:
                # If it's not in the dictionary, create a new key with an empty list as its value.
                anagram_map[sorted_i] = []

            # Append the original string "i" to the list associated with the key "sorted_i" in "anagram_map."
            anagram_map[sorted_i].append(i)

        # Convert the values of "anagram_map" (lists of anagrams) into a list and store it in "result."
        result = list(anagram_map.values())

        # Print the final result (list of lists of anagrams).
        print(result)

# Create an instance of the "Solution" class and store it in the variable "solution."
solution = Solution()

# Define the input list of strings "strs."
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Call the "groupAnagrams" method of the "solution" object with the input "strs."
solution.groupAnagrams(strs)
