class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("U") == moves.count("D") and moves.count("R") == moves.count("L"):
            return True
        return False



class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for char in moves:
            if char == "R":
                x += 1
            elif char == "L":
                x -= 1
            elif char == "U":
                x += 1
                y += 1
            elif char == "D":
                x -= 1
                y -= 1
        
        return x == y == 0