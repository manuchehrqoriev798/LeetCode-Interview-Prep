class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a regular dictionary
        res = {}

        # Iterate through each word in the input list
        for word in strs:
            # Initialize a list to represent the count of each character in the current word
            count = [0] * 26

            # Count the occurrences of each character in the current word
            for char in word:
                count[ord(char) - ord('a')] += 1

            # Convert the count list to a tuple and use it as a key to group anagrams
            key = tuple(count)

            # Check if the key exists in the dictionary
            if key in res:
                res[key].append(word)
            else:
                # If the key doesn't exist, initialize a new list for that key
                res[key] = [word]

        # Return the values (groups of anagrams) from the dictionary
        return list(res.values())



 class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        result = []

        for word in strs:

            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = []
            
            anagram_dict[sorted_word].append(word)
        
        result = list(anagram_dict.values())

        return result



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return d.values()