class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            total = digits[i] + carry
            carry = total // 10
            reminder = total % 10
            digits[i] = reminder
        
        if carry == 0:
            return digits
        else:
            return [carry] + digits
