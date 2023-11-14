class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list to store all subsets
        res = []

        # Initialize the current subset
        subset = []

        # Define a depth-first search (DFS) function
        def dfs(i):
            # Base case: if the current index is beyond the length of nums
            if i >= len(nums):
                # Add a copy of the current subset to the result list
                res.append(subset.copy())
                return
            
            # Decision: include nums[i] in the subset
            subset.append(nums[i])
            
            # Recursively call DFS for the next index
            dfs(i + 1)
            
            # Decision: do NOT include nums[i] in the subset
            subset.pop()
            
            # Recursively call DFS for the next index
            dfs(i + 1)
        
        # Start DFS from index 0
        dfs(0)
        
        # Return the list of all subsets
        return res