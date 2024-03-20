from typing import List, Tuple

class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int, int]]) -> bool:
        if not intervals:
            return True
        
        # Separate start times and end times into two separate lists
        start_times = [interval[0] for interval in intervals]
        end_times = [interval[1] for interval in intervals]
        
        # Sort both lists
        start_times.sort()
        end_times.sort()
        
        # Iterate through the sorted intervals
        for i in range(1, len(intervals)):
            # If the start time of the current interval is less than or equal to
            # the end time of the previous interval, there is a conflict
            if start_times[i] < end_times[i-1]:
                return False
        
        return True

intervals1 = [(0, 30), (5, 10), (15, 20)]
solution = Solution()
print(solution.minMeetingRooms(intervals1))  # Output: False

intervals2 = [(5, 8), (9, 15)]
print(solution.minMeetingRooms(intervals2))  # Output: True
