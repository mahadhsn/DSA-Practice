# O(n) solution
# Topics: Stack

def isValid(self, s):
    paranthesis = {'(':')','[':']','{':'}'}

    if len(s) < 2:
        return False

    stack = []
    for char in s:
        if char in paranthesis:
            stack.append(char)
        
        if char in paranthesis.values():
            if len(stack) == 0:
                return False
            elif paranthesis[stack[-1]] == char:
                stack.pop()
                continue
            else:
                return False

    if len(stack) != 0:
        return False

    return True