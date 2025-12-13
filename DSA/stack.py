# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, element):
#             self.stack.append(element)

#     def is_empty(self):
#          return len(self.stack) == 0
    
#     def pop(self):
#          if self.is_empty():
#               return "Stack is empty"
#          return self.stack.pop()
    
#     def peek(self):
#          return self.stack[-1]
    
#     def size(self):
#          return len(self.stack)
    
# my_stack = Stack()
# my_stack.push(12)
# my_stack.push(34)
# my_stack.push(43)
# my_stack.push(64)

# print(f"Original Stack : {my_stack.stack}")
# print(f"Popped element : {my_stack.pop()}")
# print(f"Stack after pop : {my_stack.stack}")
# print(f"Accessed element : {my_stack.peek()}")
# print(f"Size of stack : {my_stack.size()}")

    




















stack = []

# Push
stack.append('45')
stack.append('4')
stack.append('12')

#Original stack after insert
print("Stack: ", stack)

# Pop
element = stack.pop()
print("Pop: ", element)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))