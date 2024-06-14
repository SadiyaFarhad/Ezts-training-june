"""
Advance sub array problem : 
You are competing in a basketball contest. In this contest the score for each successful shot 
depends on both the distance from the basket and the player's position. The ball is shot N 
times, successfully. You are given an array A containing the distance of a player from basket 
for N shots. The index of array represents the position of the player. 
Score is calculated by multiplying the position with the distance from the basket.  
Your task is to find and return an integer value, representing the maximum possible score 
you can achieve by choosing a contiguous subarray of size K from the given array.  
"""

inp1=int(input("Enter number of shots made by player : "))
inp2=int(input("Enter the size of subarray : "))
arr=list(map(int,input("Enter array :").split()))
mx=-1
for i in range(0,len(arr)-inp2+1):
    temp=arr[i:i+inp2]
    k,s=1,0
    for j in temp:
       s+=(j*k)
       k+=1 
    if s>mx:
        mx=s
print("The maximum score: ",mx)
"""OUTPUT :
            Enter number of shots made by player : 5
            Enter the size of subarray : 2
            Enter array :1 2 3 4 5
            The maximum score : 14
"""