# lowkey cheating by using deque but it works
from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        students = deque(students)
        sandwiches = deque(sandwiches)  

        while True:
            if students[0] == sandwiches[0]:
                students.popleft() 
                sandwiches.popleft()  
            else:
                students.append(students.popleft())

            if (sandwiches and sandwiches[0] not in students) or not sandwiches:
                break

        return len(students)
    
# below is my original non-deque solution
class Solution1(object):
    def countStudents1(self, students, sandwiches):
        
        while(True):

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students[0])
                students.pop(0)

            if (sandwiches and sandwiches[0] not in set(students)) or (len(sandwiches)==0):
                break

        return len(students)