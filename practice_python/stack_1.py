class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is empty!!!")
            return 0
        else:
            print("Data is present in the Stack")
            return 1
            
    def display(self):
        print("Updated stack is ", self.stack)
        
    def adding(self, element):
        self.stack.append(element)
        print("Element added successfully")
        self.display()
        return True
        
    def removeElement(self):
        if self.isEmpty() >= 1:
            self.stack.pop()
            print("Element removed successfully")
            self.display()
            return True
        
obj = Stack()

obj.isEmpty()
print()
obj.adding(10)
obj.adding(20)
obj.adding(30)
obj.adding(40)
print()