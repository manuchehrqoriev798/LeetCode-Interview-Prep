class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list of numbers to a set for faster lookup
        num_set = set(nums)

        max_length = 0

        for num in nums:
            # Check if the num - 1 is not in the set. Why? because if it was then num is not the start value
            if (num - 1) not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)
        
        return max_length
        
        
        # num_set = set(nums)

        # longest = 0

        # for num in num_set:
        #     if (num-1) not in num_set:
        #         length = 0
                
        #         while (num + length) in num_set:
        #             length += 1
                
        #         longest = max(length, longest)

        # return longest
        
        


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0

                while (num + 1) in numSet:
                    length += 1
                    num = num + 1
                
                res = max(res, length + 1)
        
        return res
        
        
        
        





class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0

                while (num + 1) in numSet:
                    length += 1
                    num = num + 1
                
                res = max(res, length + 1)
        
        return res







class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0

                while (num + length) in numSet:
                    length += 1
                
                res = max(res, length)
        
        return res