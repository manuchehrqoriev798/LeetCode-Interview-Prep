class Solution:
    def combinationSum2(self, candidates, target):
        # Sort the candidates to handle duplicates
        candidates.sort()
        
        # Initialize the result list
        res = []

        # Define the recursive function for backtracking
        def backtrack(start, cur, remaining):
            # Base case: if the remaining target is 0, add the current combination to the result
            if remaining == 0:
                res.append(cur[:])
                return
            
            # Iterate through the remaining candidates
            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Skip if the current candidate is greater than the remaining target
                if candidates[i] > remaining:
                    break

                # Include the current candidate in the combination
                cur.append(candidates[i])

                # Recursively call the backtrack function for the next index
                backtrack(i + 1, cur, remaining - candidates[i])

                # Backtrack: remove the last element to explore other possibilities
                cur.pop()

        # Start the backtracking process
        backtrack(0, [], target)

        return res

