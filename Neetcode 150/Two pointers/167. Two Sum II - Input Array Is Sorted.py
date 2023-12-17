class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, (len(numbers)-1)
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum==target: 
                return [l + 1, r + 1]
            if sum > target:
                r -= 1
            elif sum < target: 
                l += 1
        return []


class Solution:
    def twoSum(self, numbers, target):
        num_dict = {}
        for i, num in enumerate(numbers):
            complement = target - numbers[i]

            if complement in num_dict:
                return [num_dict[complement]+1, i+1]
            num_dict[num] = i
        return [-1, -1]