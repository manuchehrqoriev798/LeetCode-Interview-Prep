class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize an empty list to store the maximum values for each sliding window
        res = []
        
        # Use a deque (double-ended queue) to store indices of elements in the current window
        q = collections.deque()

        # Initialize pointers for the left and right boundaries of the sliding window
        l = r = 0

        # Iterate through the entire list
        while r < len(nums):
            # Remove indices from the back of the deque if the corresponding values are smaller than the current value
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Add the current index to the deque
            q.append(r)

            # Check if the left boundary is out of the current window; if yes, remove it from the deque
            if l > q[0]:
                q.popleft()
            
            # Check if the window size has reached 'k'; if yes, append the maximum value to the result list
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            # Move the right boundary to the next element
            r += 1
        
        # Return the list of maximum values for each sliding window
        return res

    







class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use a deque (double-ended queue) to store indices of elements in the current window
        q = deque()
        # Initialize an empty list to store the maximum values for each sliding window
        res = []

        # Initialize the left boundary pointer
        l = 0

        # Iterate through the list with the help of enumerate to get both index and value
        for r, num in enumerate(nums):
            # Remove indices from the back of the deque if the corresponding values are smaller than the current value
            while q and num > nums[q[-1]]:
                q.pop()
            # Add the current index to the deque
            q.append(r)

            # Check if the left boundary is out of the current window; if yes, remove it from the deque
            if l > q[0]:
                q.popleft()

            # Check if the window size has reached 'k'; if yes, append the maximum value to the result list
            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1

        # Return the list of maximum values for each sliding window
        return res

        















# Does not pass the time limit
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        l = 0

        res = []

        for r in range(0, len(nums) - k + 1):
            maximum = max(nums[l:(r + k)])
            res.append(maximum)
            l += 1
        
        return res