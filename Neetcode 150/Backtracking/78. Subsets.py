class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # DFS 
        res = []

        subset = []

        def dfs(i):
            # Base case: if the current index is beyond the length of nums
            if i >= len(nums):
                # Add a copy of the current subset to the result list
                res.append(subset.copy())
                return
            
            # Decision: include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision: do NOT include nums[i] in the subset
            subset.pop()
            dfs(i + 1)
        
        # Start DFS from index 0
        dfs(0)
        
        return res      # Recursively call DFS for the next index






class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  
        queue = [[]] 

        while queue:
            current_subset = queue.pop(0)  # Take the first subset from the queue
            res.append(current_subset)  # Add the current subset to the result list

            for num in nums:
                if not current_subset or num > current_subset[-1]:
                    # If the current subset is empty or the current number is greater than the last element
                    # in the current subset, create a new subset by adding the current number
                    new_subset = current_subset + [num]
                    queue.append(new_subset)  # Add the new subset to the queue for further exploration

        return res  








class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in nums:
            # Create new subsets by adding the current element to existing subsets in res
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [i])
            
            # Append the newly created subsets to the result list
            res.extend(new_subsets)

        return res
