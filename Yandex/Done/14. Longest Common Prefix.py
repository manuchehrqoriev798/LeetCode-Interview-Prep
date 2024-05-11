class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return res
            res += word[i]
        
        return res



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i < len(word) and word[i] == strs[0][i]:
                    continue
                else:
                    return res
            
            res += word[i]
        
        return res