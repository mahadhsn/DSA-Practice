# good enough bruh
class Solution(object):

    def isValid(self, s):
        paranthesis = {'(':')','[':']','{':'}'}
        open_symbols = ["(", "[", "{"]

        if len(s) < 2:
            return False

        stack = []
        for char in s:
            if char in open_symbols:
                stack.append(char)
            
            if char in paranthesis.values():
                if not stack:
                    return False
                if char != paranthesis[stack[-1]]:
                    return False
                stack.pop()

        if stack:
            return False

        return True