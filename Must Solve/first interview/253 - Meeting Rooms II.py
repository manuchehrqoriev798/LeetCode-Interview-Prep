from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Separate the start times and end times into separate lists
        start_times = sorted(interval[0] for interval in intervals)
        end_times = sorted(interval[1] for interval in intervals)
        
        num_rooms = 0
        end_pointer = 0
        
        # Iterate through each start time
        for start_time in start_times:
            # If the current start time is after the end time of the earliest ongoing meeting, reuse that room
            if start_time >= end_times[end_pointer]:
                end_pointer += 1
            else:
                # Otherwise, a new room is needed
                num_rooms += 1
        
        return num_rooms

# Test cases
intervals1 = [(0, 30), (5, 10), (15, 20)]
intervals2 = [(2, 7)]

sol = Solution()
print(sol.minMeetingRooms(intervals1))  # Output: 2
print(sol.minMeetingRooms(intervals2))  # Output: 1
