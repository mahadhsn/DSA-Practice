# another (more efficient) way to create a stack in python
from collections import deque

stack = deque()

stack.append("Minecraft")
stack.append("COD")
stack.append("FH5")
stack.append("Rocket League")
print(stack)


stack.pop()
print(stack)
print(stack[-1])