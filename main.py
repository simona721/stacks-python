#Initializing an empty stack

stack = []

#Adding elements to the stack

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
stack.append(7)
stack.append(8)
stack.append(9)
stack.append(10)

print(f"Initial stack: {stack}")

#Poping the elements from the stack in the LIFO order
print("Poped elements: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(f"The stack after the poped elements: {stack}")