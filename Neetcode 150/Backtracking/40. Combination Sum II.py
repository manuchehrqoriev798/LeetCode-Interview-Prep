class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            # Base cases
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            
            cur.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res







class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        
        res = []

        def backtrack(start, cur, target):
            if target == 0:
                res.append(cur[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break

                # Include the current candidate in the combination
                cur.append(candidates[i])

                # Recursively call the backtrack function for the next index
                backtrack(i + 1, cur, target - candidates[i])

                # Backtrack: remove the last element to explore other possibilities
                cur.pop()

        backtrack(0, [], target)

        return res











class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        
        res = []

        def backtrack(start, cur, target):
            if target == 0:
                res.append(cur.copy())

            
            prev = None
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                
                if candidates[i] > target:
                    break
                
                cur.append(candidates[i])

                backtrack(i + 1, cur, target - candidates[i])

                cur.pop()

                prev = candidates[i]


        backtrack(0, [], target)

        return res