class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        ans = ""
        sign = ""
        for i in range(n):
            if s[i] == '-' or s[i] == '+':
                if sign or ans:
                    break
                sign = s[i]
            elif s[i] == '"' or s[i] == " ":
                if ans or sign:
                    break
            elif s[i].isdigit():
                ans += s[i]
            else:
                break

        if not ans:
            return 0
        ans = int(ans)
        if sign == "-":
            ans = -ans
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans







class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        i, num, sign = 0, 0, 1

        if s[0] == '+' or s[0] == '-':
            sign = -1 if s[0] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            num = num * 10 + digit
            i += 1

        return sign * num









