class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0

        r = 0
        while seats[r] != 1:
            r += 1
        max_distance = max(max_distance, r)

        r = len(seats) - 1
        while seats[r] != 1:
            r -= 1
        max_distance = max(max_distance, len(seats) - 1 - r)

        l, r = 0, 0
        while r < len(seats):
            while r < len(seats) and seats[r] != 1:
                r += 1
            
            max_distance = max(max_distance, (r - l + 1) // 2)

            r += 1
            l = r

        return max_distance






# No comment this one was really hard:
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0

        l, r = 0, 0
        while r < len(seats):
            while r < len(seats) and seats[r] != 1:
                r += 1
            
            if l == 0 and seats[l] == 0:
                max_distance = max(max_distance, r)  
            elif r == len(seats) and seats[r-1] == 0:
                max_distance = max(max_distance, len(seats) - l)  
            else:
                max_distance = max(max_distance, (r - l + 1) // 2) 

            r += 1
            l = r

        return max_distance
