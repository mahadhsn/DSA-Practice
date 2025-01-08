
# Topics: Queue, Stack, Array, Simulation
def countStudents(students, sandwiches):
    while(True):

        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            students.append(students[0])
            students.pop(0)

        if (sandwiches and sandwiches[0] not in students) or not sandwiches:
            break

    return len(students)

# better version
# beats 100% of users on LeetCode
from collections import deque

def countStudentsDeque(students, sandwiches):
    students = deque(students)  # Convert students list to deque
    sandwiches = deque(sandwiches)  # Convert sandwiches list to deque

    while True:
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
        else:
            students.append(students.popleft())

        if (sandwiches and sandwiches[0] not in students) or not sandwiches:
            break

    return len(students)