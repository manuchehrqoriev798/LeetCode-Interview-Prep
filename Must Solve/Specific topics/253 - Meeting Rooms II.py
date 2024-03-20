from typing import List, Tuple
from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int, int]]) -> int:
        if not intervals:
            return 0
        
        # Separate start times and end times into two separate lists
        start_times = sorted(interval[0] for interval in intervals)
        end_times = sorted(interval[1] for interval in intervals)
        
        # Initialize pointers and room count
        start_ptr = end_ptr = 0
        rooms_required = 0
        max_rooms = 0
        
        # Iterate through both lists
        while start_ptr < len(start_times):
            # Check for overlap
            if start_times[start_ptr] < end_times[end_ptr]:
                rooms_required += 1
                max_rooms = max(max_rooms, rooms_required)
                start_ptr += 1
            else:
                rooms_required -= 1
                end_ptr += 1
        
        return max_rooms

intervals1 = [(0, 30), (5, 10), (15, 20)]
solution = Solution()
print(solution.minMeetingRooms(intervals1))
