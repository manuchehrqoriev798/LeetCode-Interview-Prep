class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        
        while r < len(chars):
            target_char = chars[r]
            count = 0
            
            while r < len(chars) and chars[r] == target_char:
                r += 1
                count += 1     
            
            chars[l] = target_char
            l += 1
            
            if count > 1:
                for digit in str(count):
                    chars[l] = digit
                    l += 1
                    
        return l








