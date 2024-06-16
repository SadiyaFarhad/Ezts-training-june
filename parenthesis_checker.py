"""
Develop a Python program to check if the parentheses in a given mathematical expression are balanced. 
The expression may contain different types of parentheses: round (), curly {}, and square [].
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
e="[3+7{52/11(3+5)}]"
s=stack()
ob="[{("
cb=")}]"
flag=0
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
        x=s.pop()
        if x=="(" and i==")":
            pass
        elif x=="{" and i=="}":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag=1
            break
if flag==0 and s.size()==0:
    print("valid ")
else:
    print("invalid")
        #best way to use is dictionary    
print(s.size())

#Output: 
#valid 
#0
