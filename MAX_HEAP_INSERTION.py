# MAX HEAP INSERTION
l=[]
p=list(map(int,input("enter the element to store: ").split(" ")))
for i in p: 
    l.append(i)
    print(l)
    i=len(l)-1
    while i>0:
       if l[i]>l[i//2]:
           l[i//2],l[i]=l[i],l[i//2]
           i=i//2
       else:
         break
print(l)
#OUTPUT
enter the element to store: 4 3 2 1 9 5 6 7
[4]
[4, 3]
[4, 3, 2]
[4, 3, 2, 1]
[4, 3, 2, 1, 9]
[9, 4, 3, 1, 2, 5]
[9, 5, 4, 1, 2, 3, 6]
[9, 6, 4, 5, 2, 3, 1, 7]
[9, 7, 4, 6, 2, 3, 1, 5]

        
    
