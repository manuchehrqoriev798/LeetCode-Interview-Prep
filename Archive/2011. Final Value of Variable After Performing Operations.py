class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                count -= 1
            else:
                count += 1
        
        return count

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for i in range(len(operations)):
            if "--" in operations[i]:
                count -= 1
            else:
                count += 1
        
        return count
