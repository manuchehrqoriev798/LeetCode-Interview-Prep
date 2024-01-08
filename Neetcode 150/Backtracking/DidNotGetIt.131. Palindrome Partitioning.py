class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    backtrack(j + 1)
                    part.pop()
        backtrack(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True





class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(cur_part, start):
            if len(s) == start:
                res.append(cur_part)
                return

            for end in range(start, len(s)):
                cur_substring = s[start:end + 1]

                if cur_substring == cur_substring[::-1]:
                    backtrack(cur_part + [cur_substring], end + 1)

        backtrack([], 0)

        return res










class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(start):
            if len(s) == start:
                res.append(part.copy())
                return

            for end in range(start, len(s)):
                cur_substring = s[start:end + 1]

                if cur_substring == cur_substring[::-1]:
                    part.append(cur_substring)
                    backtrack(end + 1)
                    
                    part.pop()

        backtrack(0)

        return res
