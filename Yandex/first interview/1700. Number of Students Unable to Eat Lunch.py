class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        
        while len(students) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                count += 1
                students.append(students.pop(0))
            
            if count == len(students):
                return count
        
        return 0




class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for s in sandwiches:
            if s in students:
                students.remove(s)
            else:
                break
        return len(students)