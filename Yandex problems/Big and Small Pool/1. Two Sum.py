class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        sorted_num = sorted(nums)

        while l <= r:
            cur = sorted_num[l] + sorted_num[r]

            if cur == target:
                index1, index2 = -1, -1

                for i in range(len(nums)):
                    if index1 == -1 and sorted_num[l] == nums[i]:
                        index1 = i
                    elif sorted_num[r] == nums[i]:
                        index2 = i
                    
                return [index1, index2]
        

            elif cur > target:
                r -= 1
            else:
                l += 1
            



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[num] = i



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[num] = i





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        sorted_nums = sorted(nums)

        while l != r:
            current_sum = sorted_nums[l] + sorted_nums[r]

            if current_sum == target:
                index1 = -1
                index2 = -1
                for i in range(len(nums)):
                    # Check if the current element in 'nums' is equal to the leftmost element in sorted order. Also, ensure that the index for the leftmost element has not been found yet.
                    if nums[i] == sorted_nums[l] and index1 == -1:
                        index1 = i
                    elif nums[i] == sorted_nums[r]:
                        index2 = i

                # Return a list containing the indices of the elements that contribute to the target sum.
                return [index1, index2]

            elif current_sum > target:
                r -= 1
            else:
                l += 1