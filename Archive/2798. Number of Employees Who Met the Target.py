class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                count += 1
        return count


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        for i in range(len(hours)):
            if hours[i] >= target:
                return len(hours) - i
        return 0


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len(list(filter(lambda x: x >= target, hours)))