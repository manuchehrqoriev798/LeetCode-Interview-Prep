class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def remove(s, start_i, start_j, open_paren, close_paren):
            num_open, num_close = 0, 0
            for i in range(start_i, len(s)):
                if s[i] == open_paren:
                    num_open += 1
                if s[i] == close_paren:
                    num_close += 1
                if num_close > num_open: 
                    for j in range(start_j, i + 1):
                        if s[j] == close_paren and (j == start_j or s[j-1] != close_paren):
                            remove(s[:j] + s[j+1:], i, j, open_paren, close_paren)
                    return  
                
            reversed_s = s[::-1]
            if open_paren == '(':
                remove(reversed_s, 0, 0, ')', '(')
            else:
                output.append(reversed_s)
                
        output = []
        remove(s, 0, 0, '(', ')')
        return output

        