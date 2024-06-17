"""
Create a Stack class in Python that represents a stack data structure.
A stack is a collection of elements with two principal operations:
Push: Adds an element to the top of the stack.
Pop: Removes and returns the top element of the stack.
The stack should also provide a method to return the current size of the stack
"""
class stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
         #use value in push and accept value by formal variable to store data 
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.items)
print(s.pop())
print(s.items)
print(s.size())

"""
Output:
[10, 20, 30, 40, 50]
50
[10, 20, 30, 40]
4
"""    