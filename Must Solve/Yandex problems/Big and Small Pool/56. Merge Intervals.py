class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        res = []

        for i in intervals:
            if len(res) == 0:
                res.append(i)
            else:
                last = res[len(res) - 1]

                if last[1] < i[0]:
                    res.append(i)
                else:
                    # last[1] = max(last[1], i[1])
                    last[:] = [last[0], max(last[1], i[1])]
                    # res[len(res) - 1] = [last[0], max(last[1], i[1])]
        
        return res