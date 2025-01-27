old = [1,2,3,4,5]

def copy(oldStack):
    newStack = []
    temp = []
    
    while oldStack:
        temp.append(oldStack.pop())
        print(oldStack)
        print(temp)
    
    while temp:
        value = temp.pop()
        newStack.append(value)
        oldStack.append(value)
        print("Old stack: ",oldStack)
        print("new stack: ",newStack)
        print("temp: ",temp)

    return newStack

print(old)
print(copy(old))