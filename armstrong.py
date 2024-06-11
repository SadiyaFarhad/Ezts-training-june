
"""
 Program for checking whether Armstrong Number or not
Created on Tue Jun 11 19:54:20 2024

@author: Sadiya Farhad
"""
n=7645 #to check whether 7645 is armstrong number
count=0 #to count digits of 7645 i.e 4
org=0 #to indicate orginal value i.e 0
n1=0 #to used n1 in while loop 

# Calculate the number of digits in the number
while n>0:
    count=count+1
    n=n//10
    ans=0 
# Calculate Armstrong number
while n1>0:
    digit=n%10
    p=digit**count
    ans=ans+p
    n=n//10
# Check if the number is Armstrong or not
if ans==org:
    print("armstrong number")
else:
    print("Not armstrong number")


