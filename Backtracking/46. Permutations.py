class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            cur_num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(cur_num)
            res.extend(perms)
            nums.append(cur_num)

        return res






        # res = []

        # def dfs(i, cur):
        #     if i == len(nums):
        #         res.append(cur.copy())
        #         return

        #     for j in range(i, len(nums)):
        #         cur.append(nums[j])
        #         nums[i], nums[j] = nums[j], nums[i]  
        #         dfs(i + 1, cur)
        #         cur.pop()
        #         nums[i], nums[j] = nums[j], nums[i] 

        # dfs(0, [])
        # return res
