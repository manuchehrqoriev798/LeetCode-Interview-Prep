class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p, s in zip(position, speed):
            pair.append([p, s])


        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

from typing import List




class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0

        cars = sorted(zip(position, speed), reverse=True)

        last_fleet_time = float('-inf')  # Initialize to negative infinity

        for car in cars:
            car_p, car_s = car

            time = (target - car_p) / car_s

            if time > last_fleet_time:
                last_fleet_time = time
                fleet_count += 1
        
        return fleet_count


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize the count of fleets
        fleet_count = 0

        # Combine position and speed into a list of tuples and sort it in descending order based on position
        cars = sorted(zip(position, speed), reverse=True)

        # Variable to store the time of the last fleet (initially set to None)
        last_fleet_time = None

        # Iterate through each car in the sorted list
        for car in cars:
            # Extract position and speed from the tuple
            car_position, car_speed = car

            # Calculate the time it takes for the car to reach the target
            time_to_reach_target = (target - car_position) / car_speed

            # Check if there was no last fleet or the current car reaches the target later than the last fleet
            if not last_fleet_time or time_to_reach_target > last_fleet_time:
                # Update the last fleet time to the current car's arrival time
                last_fleet_time = time_to_reach_target

                # Increment the fleet count since the current car is part of a new fleet
                fleet_count += 1

        # Return the total count of fleets
        return fleet_count










class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)





class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(map(list, zip(position, speed)))

        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)




class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []

        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        pairs = sorted(pairs)[::-1]

        for p,s in pairs:
            time = (target - p) / s
            stack.append(time)
        
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
