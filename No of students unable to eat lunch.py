class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        iterations = 0
        while iterations < len(sandwiches):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                iterations = 0
                continue
            back_s = students[0]
            students = students[1:]
            students.append(back_s)
            iterations += 1
        return len(students)
