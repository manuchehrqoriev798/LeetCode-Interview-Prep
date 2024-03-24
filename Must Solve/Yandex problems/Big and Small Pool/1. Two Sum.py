class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            total = sorted_nums[l] + sorted_nums[r]
            if total == target:
                index1, index2 = -1, -1
                for i in range(len(nums)):
                    if index1 == -1 and nums[i] == sorted_nums[l]:
                        index1 = i
                    elif nums[i] == sorted_nums[r]:
                        index2 = i
                return [index1, index2]
            elif total > target:
                r -= 1
            else:
                l += 1
        