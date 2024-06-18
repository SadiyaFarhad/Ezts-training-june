#SELECTION SORT

l=[9,7,5,8,10,26,44,3,1]
n=len(l)
for j in range(0,n):
    pos=j
    min=l[j]
    for i in range(j,n):
        if l[i]<min:
            min=l[i]
            pos=i
    l[j],l[pos]=l[pos],l[j]
print("the sorted array is : ",l)
#OUTPUT : the sorted array is :  [1, 3, 5, 7, 8, 9, 10, 26, 44]