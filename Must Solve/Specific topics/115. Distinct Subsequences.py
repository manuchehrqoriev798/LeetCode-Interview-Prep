class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Initialize a memoization dictionary to store computed results
        memory = {}

        # Define a recursive function to perform depth-first search
        def dfs(i, j):
            # Base cases:
            # If j reaches the end of t, we found a valid subsequence, return 1
            if j == len(t):
                return 1
            # If i reaches the end of s but j hasn't reached the end of t,
            # it's not possible to form the subsequence, return 0
            if i == len(s):
                return 0
            # If the result for current (i, j) pair is already computed,
            # return it from the memory dictionary
            if (i, j) in memory:
                return memory[(i, j)]

            # If s[i] equals t[j], we have two choices:
            if s[i] == t[j]:
                # Include s[i] in the subsequence and recursively explore the next characters
                # by calling dfs with incremented i and j, and add it with excluding s[i]
                memory[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # If s[i] doesn't equal t[j], exclude s[i] from the subsequence
                # and only move forward in s
                memory[(i, j)] = dfs(i + 1, j)
            # Return the computed result for current (i, j) pair
            return memory[(i, j)]

        # Start the depth-first search from the initial positions (0, 0)
        return dfs(0, 0)