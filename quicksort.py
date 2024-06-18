#QUICK SORT IMPLEMENTATION

def divide(l,low,high):
    p=l[high]
    pi=high
    j=low-1
    for i in range(low,high): 
        if l[i]<=p: 
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[j],l[pi]=l[pi],l[j]
    pi=j
    return pi
def quick_sort(l,low,high):
    if low<high:
        pi=divide(l,low,high)#find pi
        print(pi,low,high)#W2
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
    return
if __name__=="__main__":
    l=list(map(int,input("Enter elements to sort: ").split()))
    low=0
    high=len(l)-1
    print(low,high)
    quick_sort(l,low,high)
    print("sorted array =",l)
    #4 2
    
"""
OUTPUT:
Enter elements to sort: 5 3 2 1 6 4
0 5
3 0 5
0 0 2
2 1 2
4 4 5
sorted array = [1, 2, 3, 4, 5, 6]
"""