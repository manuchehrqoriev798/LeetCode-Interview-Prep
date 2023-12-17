class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # This one is little bit faster and takes less space than the second solution
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return fast



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solving with constant extra space - Floyd's algorithm

        # Initialize two pointers, slow and fast, both starting at the beginning of the array.
        slow, fast = 0, 0

        # Start a loop that continues until a cycle is detected in the array.
        while True:
            # Move slow one step ahead.
            slow = nums[slow]
            # Move fast two steps ahead.
            fast = nums[nums[fast]]

            # If slow and fast meet at the same value, a cycle is detected, so exit the loop.
            if slow == fast:
                break

        # After exiting the first loop, initialize a new pointer, slow2, at the beginning of the array.
        slow2 = 0

        # Start a new loop to find the actual duplicate value.
        while True:
            # Move slow2 one step ahead.
            slow2 = nums[slow2]
            # Move slow one step ahead.
            slow = nums[slow]

            # When slow2 and slow meet at the same value, it indicates the duplicate value, so return it.
            if slow2 == slow:
                return slow








class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using set
        setNums = set()
        for i in range(nums):
            if nums[i] not in setNums:
                setNums.add(nums[i])
            else:
                return i
        return -1



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using Hashmap 
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        for num, count in num_counts.items():
            if count > 1:
                return num

        return -1