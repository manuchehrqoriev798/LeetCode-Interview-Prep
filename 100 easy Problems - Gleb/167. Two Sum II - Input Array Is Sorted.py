class Solution:
    def twoSum(self, numbers, target):
        hashmap = {}

        for index, num in enumerate(numbers):
            hashmap[num] = index
        
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in hashmap:
                return [i + 1, hashmap[complement] + 1]



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, (len(numbers)-1)
        while l < r:
            total = numbers[l] + numbers[r]
            if total==target: 
                return [l + 1, r + 1]
            if total > target:
                r -= 1
            elif total < target: 
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


class Solution:
    def twoSum(self, numbers, target):
        hashmap = {}

        for index, num in enumerate(numbers):
            hashmap[num] = index
        
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in hashmap:
                return [i + 1, hashmap[complement] + 1]
