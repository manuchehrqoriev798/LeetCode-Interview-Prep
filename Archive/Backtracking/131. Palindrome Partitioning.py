class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def backtracking(temp, i):
            if len(s)==i:
                ans.append(temp)
                return
            for j in range(i, len(s)):
                res=s[i:j+1]
                if res==res[::-1]:
                    backtracking(temp+[res], j+1)
            return
        backtracking([], 0)
        return ans