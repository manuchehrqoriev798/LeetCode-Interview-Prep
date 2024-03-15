class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0

        while r < len(chars):
            target = chars[r]
            count = 0

            while r < len(chars) and chars[r] == target:
                r += 1
                count += 1
            
            chars[l] = target
            l += 1

            if count > 1:
                for digit in str(count):
                    chars[l] = digit
                    l += 1
            
        return l