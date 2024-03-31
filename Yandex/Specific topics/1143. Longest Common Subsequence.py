class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Helper function for recursive traversal
        def lcsHelper(i, j):
            # Base case: if either string is empty, return 0
            if i == len(text1) or j == len(text2):
                return 0
            
            # If the current indices are memoized, return the result
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If characters match, increment both indices
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcsHelper(i + 1, j + 1)
            else:
                # If characters don't match, try two possibilities:
                # 1. Skip a character from text1
                # 2. Skip a character from text2
                memo[(i, j)] = max(lcsHelper(i + 1, j), lcsHelper(i, j + 1))
            
            return memo[(i, j)]
        
        # Initialize memoization hashmap
        memo = {}
        
        # Start recursive traversal from index 0 of both strings
        return lcsHelper(0, 0)





