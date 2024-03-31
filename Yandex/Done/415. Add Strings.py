class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def convertStrToInteger(num):
            newNum = 0
            for i in range(len(num)):
                newNum = newNum * 10 + int(num[i])
            
            return newNum
        
        return str(convertStrToInteger(num1) + convertStrToInteger(num2))
