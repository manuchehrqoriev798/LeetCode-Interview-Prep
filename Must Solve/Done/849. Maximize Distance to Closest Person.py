class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDistance = 0
        count = 0
        for l in range(len(seats)):
            if seats[l] == 1:
                break
            count += 1
        maxDistance = max(maxDistance, count)

        count = 0
        for r in range(len(seats) - 1, -1, -1):
            if seats[r] == 1:
                break
            count += 1
        maxDistance = max(maxDistance, count)


        r = l
        while r < len(seats):
            if seats[r] == 1:
                maxDistance = max(maxDistance, (r - l)//2)
                l = r
            r += 1
        
        return maxDistance




class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDistance = 0
        l, r = 0, len(seats) - 1

        while seats[l] != 1:
            l += 1
        maxDistance = max(maxDistance, l)

        while seats[r] != 1:
            r -= 1
        maxDistance = max(maxDistance, len(seats) - r - 1)


        r = l
        while r < len(seats):
            if seats[r] == 1:
                maxDistance = max(maxDistance, (r - l)//2)
                l = r
            r += 1
        
        return maxDistance
