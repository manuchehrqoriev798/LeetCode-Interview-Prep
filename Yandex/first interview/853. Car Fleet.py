class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            position[i] = [target - position[i], speed[i]]
        position.sort()

        count = 0
        stack = []

        for i in range(len(position)):
            car_p, car_s = position[i]
            time = car_p / car_s

            if not stack or time > stack[-1]:
                stack.append(time)
                count += 1
        
        return count





class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            position[i] = [target - position[i], speed[i]]
        position.sort()

        fleet_count = 0
        last_fleet_time = float('-inf')

        for i in range(len(position)):
            car_p, car_s = position[i]
            time = car_p / car_s

            if time > last_fleet_time:
                last_fleet_time = time
                fleet_count += 1

        return fleet_count





class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            position[i] = [target - position[i], (target - position[i]) / speed[i]]
        position.sort()

        fleet_count = 0
        last_fleet_time = float('-inf')

        for i in range(len(position)):
            car_p, car_t = position[i]

            if car_t > last_fleet_time:
                last_fleet_time = car_t
                fleet_count += 1

        return fleet_count
    


