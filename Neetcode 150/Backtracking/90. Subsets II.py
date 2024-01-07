class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Include the current element in the subset
            subset.append(nums[i])
            # Recursively call the backtrack function for the next index
            backtrack(i + 1, subset)
            # Exclude the current element from the subset (backtrack)
            subset.pop()

            # Skip duplicates
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            # Recursively call the backtrack function for the next index after skipping duplicates
            backtrack(i + 1, subset)

        backtrack(0, [])

        return res





class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, subset):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                # Skip duplicates to avoid duplicate subsets
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Decision: include nums[i] in the subset
                subset.append(nums[i])

                # Recursively call backtrack for the next index
                backtrack(i + 1, subset)

                # Decision: do NOT include nums[i] in the subset
                subset.pop()

        backtrack(0, [])

        return res