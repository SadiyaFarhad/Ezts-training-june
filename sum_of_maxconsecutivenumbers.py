#Given an array of integers arr, find the maximum sum of three consecutive elements in the array. 
#Print the maximum sum and the three elements that contribute to this sum.
#sample input: [2,4,3,5,6,3,4,6,7,1,2,5]
#output:[17,4,6,7]

arr=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
for i in range(0,len(arr)-2):
    sum=arr[i]+arr[i+1]+arr[i+2]
    if max<sum:
        max=sum
        pos=i
print(max,arr[pos],arr[pos+1],arr[pos+2])