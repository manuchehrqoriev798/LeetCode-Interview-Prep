class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num!=0:
            if num>= 1000:
                res+='M'
                num-=1000
            elif num>= 900:
                res+='CM'
                num-=900
            elif num>= 500:
                res+='D'
                num-= 500
            elif num>= 400: 
                res+='CD' 
                num-= 400
            elif num>= 100:
                res+='C'
                num-=100
            elif num>= 90:
                res+='XC' 
                num-=90
            elif num>= 50:
                res+='L' 
                num-=50
            elif num>= 40:
                res+='XL' 
                num-=40
            elif num>= 10:
                res+='X' 
                num-=10
            elif num>= 9:
                res+='IX' 
                num-=9
            elif num>= 5:
                res+='V' 
                num-=5
            elif num>= 4:
                res+='IV' 
                num-=4
            else:
                res+='I'
                num-=1
        return res








class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        d = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
             10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
             100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC",900: "CM", 1000: "M", 2000: "MM", 3000: "MMM", 4000: "MMMM", 5000: "MMMMM", 6000: "MMMMMM", 7000: "MMMMMMM", 8000: "MMMMMMMM", 9000: "MMMMMMMMM"}
        

        numStr = str(num)
        lenNum = len(numStr)
        for i in range(lenNum):
            if int(numStr[i]) in d:
                digit = int(numStr[i])
                place_value = 10 ** (lenNum - i - 1)

                res += d[digit * place_value]
    
        return res















class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        d = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
             10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
             100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC",900: "CM", 1000: "M", 2000: "MM", 3000: "MMM", 4000: "MMMM", 5000: "MMMMM", 6000: "MMMMMM", 7000: "MMMMMMM", 8000: "MMMMMMMM", 9000: "MMMMMMMMM"}
        

        numStr = str(num)
        lenNum = len(numStr)
        for i in range(lenNum):
            digit = int(numStr[i])
            if digit == 0:
                continue
            place_value = 10 ** (lenNum - i - 1)
            res += d[digit * place_value]
    
        return res

















class Solution:
    def intToRoman(self, num: int) -> str:
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                          (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                          (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        res = ""
        for value, symbol in d:
            while num >= value:
                res += symbol
                num -= value
        return res












