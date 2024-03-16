class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count_dict = {}
        ans = []
        count = 0

        for i in range(len(A)):
            if A[i] not in count_dict:
                count_dict[A[i]] = 0
            count_dict[A[i]] += 1
            if count_dict[A[i]] == 2:
                count += 1

            if B[i] not in count_dict:
                count_dict[B[i]] = 0
            count_dict[B[i]] += 1
            if count_dict[B[i]] == 2:
                count += 1

            ans.append(count)
        
        return ans 
