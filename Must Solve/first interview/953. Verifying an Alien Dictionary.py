class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {}
        for index, char in enumerate(order):
            alien_dict[char] = index


        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            l, r = 0, 0
            while l < len(word1) and r < len(word2):
                if alien_dict[word1[l]] < alien_dict[word2[r]]:
                    break
                elif alien_dict[word1[l]] > alien_dict[word2[r]]:
                    return False
                l += 1
                r += 1
            if r == len(word2) and l < len(word1):
                return False

        return True


