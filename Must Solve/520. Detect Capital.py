class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
        # return word.isupper() or word.islower() or (word == word.capitalize())



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        word1 = sorted(word)
        if word[0].isupper():
            if word1[-1].isupper():
                return True
            elif not word1[1].isupper():
                return True
            else:
                return False
        else:
            if word1[0].isupper():
                return False
            else:
                return True
        
        return False        
        