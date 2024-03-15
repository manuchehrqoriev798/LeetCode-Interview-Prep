class Solution(object):
    def groupAnagrams(self, strs):
        anagram = {}
        res = []

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in anagram:
                anagram[sorted_word].append(word)
            else:
                anagram[sorted_word] = [word]
        
        for key, value in anagram.items():
            res.append(anagram[key])
        
        return res
