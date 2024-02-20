class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        sorted_nums = sorted(nums)

        while l <= r:
            if sorted_nums[l] + sorted_nums[r] > target:
                r -= 1
            elif sorted_nums[l] + sorted_nums[r] < target:
                l += 1
            else:
                index1 = -1
                index2 = -1

                for i in range(len(nums)):
                    if index1 == -1 and nums[i] == sorted_nums[l]:
                        index1 = i
                    elif nums[i] == sorted_nums[r]:
                        index2 = i
                
                return [index1, index2]
        
        return []