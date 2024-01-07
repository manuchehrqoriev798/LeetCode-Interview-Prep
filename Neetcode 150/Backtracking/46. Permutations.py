class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)

            # Recursively generate permutations for the remaining elements
            perms = self.permute(nums)

            # Append the current element to each generated permutation
            for perm in perms:
                perm.append(n)
            
            # Adds all permutations to the result list individually
            res.extend(perms)  
            
            # Append the current element back
            nums.append(n)     

        return res






class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums.copy()]
        
        res = []

        def backtrack(i, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 
            
            for j in range(i, len(nums)):
                # Make a choice: Append the current element
                cur.append(nums[j])
                
                # Swap nums[i] and nums[j]
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                
                # Recursively explore further
                backtrack(i + 1, cur)
                
                # Undo the choice (backtrack): Remove the last element and swap back nums[i] and nums[j]
                cur.pop()
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0, [])
        return res
