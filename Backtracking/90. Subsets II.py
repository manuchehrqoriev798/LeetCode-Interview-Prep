class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list to store all subsets
        res = []

        # Initialize the current subset
        subset = []

        # Sort the input array to handle duplicates
        nums.sort()

        # Define a depth-first search (DFS) function
        def dfs(start):
            # Add the current subset to the result list
            res.append(subset.copy())

            # Iterate through the remaining elements
            for i in range(start, len(nums)):
                # Skip duplicates to avoid duplicate subsets
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Decision: include nums[i] in the subset
                subset.append(nums[i])

                # Recursively call DFS for the next index
                dfs(i + 1)

                # Decision: do NOT include nums[i] in the subset
                subset.pop()

        # Start DFS from index 0
        dfs(0)

        # Return the list of all subsets
        return res
