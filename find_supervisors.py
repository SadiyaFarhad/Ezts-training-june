"""
I a tyre factory many workers are working there each worker is assigned with a integer number which help them to find their supervisor.
The project manager having an array that consist of a integer numbers help the project manager to find their supervisors.
Supervisor will be assigned as the first largest integer find on the right side of the array if not found return -1.

Input : [3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
Output: [5,14,14,-1,7,7,-1,9,9,-1,5,5,-1,-1]
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0

l = [3, 5, 2, 14, 5, 3, 7, 9, 4, 6, 9, 4, 2, 5, 3]
o = [0] * len(l)
s = Stack()

for i in range(len(l) - 1, -1, -1):  # reverse
    while not s.is_empty() and s.top() <= l[i]:
        s.pop()
        
    if s.is_empty():
        o[i] = -1
    else:
        o[i] = s.top()
        
    s.push(l[i])

print(o)
