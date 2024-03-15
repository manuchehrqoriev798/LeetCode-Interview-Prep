class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a list to count occurrences of each character in magazine
        counts = [0] * 26
        
        # Count occurrences of each character in magazine
        for char in magazine:
            counts[ord(char) - ord('a')] += 1
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            index = ord(char) - ord('a')
            counts[index] -= 1
            if counts[index] < 0:
                return False
        
        return True





class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}

        for char in magazine:
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1
        
        for char in ransomNote:
            if char in d1 and  d1[char] > 0:
                d1[char] -= 1
            else:
                return False
        
        return True
        

