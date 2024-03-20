class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize an empty list for cars
        cars = []

        # Iterate over each index in the range of the length of the position list
        for i in range(len(position)):
            # Create a tuple for each car with its position and speed
            car = (position[i], speed[i])
            # Append each car to the cars list
            cars.append(car)

        # Sort the cars list in ascending order based on the car's position
        cars.sort(key=lambda x: x[0])

        # Initialize the fleet count and the time of the last fleet
        fleet_count = 0
        last_fleet_time = 0

        # Iterate over the cars from the end to the start
        for i in range(len(cars)-1, -1, -1):
            car_p, car_s = cars[i]
            # Calculate the time it takes for the car to reach the target
            time = (target - car_p) / car_s

            # If the time is greater than the time of the last fleet, increment the fleet count
            if time > last_fleet_time:
                last_fleet_time = time
                fleet_count += 1

        return fleet_count






class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0

        cars = sorted(zip(position, speed), reverse=True)

        last_fleet_time = float('-inf')

        for car in cars:
            car_p, car_s = car

            time = (target - car_p) / car_s

            if time > last_fleet_time:
                last_fleet_time = time
                fleet_count += 1
            
        
        return fleet_count
    


