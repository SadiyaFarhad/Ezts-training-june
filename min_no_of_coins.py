Available denominators :- 1,5,7
Bill amount=18
What will be the min number of coins required to pay the bill using GREEDY APPROACH.  
l=[7,5,1]
b=0
c=0
i=0
while(b>0):
    if b>=l[i] and i<len(l):
        c+=1
        b=b-l[i]
    else:
        i+=1
print(c)
OUTPUT:
6
