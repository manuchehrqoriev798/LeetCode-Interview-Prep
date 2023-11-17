class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            # Iterate through the remaining elements
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Decision: include nums[i] in the subset
                cur.append(candidates[i])

                # Recursively call DFS for the next index
                dfs(i, cur, total + candidates[i])
                

                # Decision: do NOT include nums[i] in the subset
                cur.pop()

        dfs(0, [], 0)
        return res
