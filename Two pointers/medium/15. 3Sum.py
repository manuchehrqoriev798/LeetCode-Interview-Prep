class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        result = []
        for i, a in enumerate(s_nums):
            if i > 0 and a == s_nums[i-1]:
                continue

            l, r = i + 1, len(s_nums)-1
            while l < r:
                threeSum = a + s_nums[l] + s_nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, s_nums[l], s_nums[r]])         # adds solution to result
                    l += 1                                           # changes l pointer in order to continue
                    while s_nums[l]==s_nums[l-1] and l < r:          # checks if there are two neighbors so it will just skip them by incrementing l
                        l += 1
        return result