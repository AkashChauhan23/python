class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def pop(self):
        if self.stack != []:
            return self.stack.pop()
        else:
            return "No data found!!!"
    
    def top(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            return "Stack is empty!!!"

    def displayStack(self):
        if len(self.stack) > 0:
            return self.stack
        else:
             return "No data to display!!!"
obj = Stack()

# Data pushing to stack
obj.push("January")
obj.push("February")
obj.push("March")

# Display full stack
print(obj.displayStack())

# Data pop from stack
print(obj.pop())

# Element on top
print(obj.top())

# Display full stack
print(obj.displayStack())