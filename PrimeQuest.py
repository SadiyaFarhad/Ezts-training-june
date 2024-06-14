"""Your task is to write a function that takes an integer N and returns a tuple 
containing the following: 
- The smallest prime number larger than N (Level 1 result). 
- The sum of all prime numbers between N and the smallest prime number 
larger than N (Level 2 result). 
- A boolean indicating whether the product of the smallest prime number larger than N and the next immediate prime number is prime (Level 3 result). 
Help Alice navigate through the levels, solve the puzzle, and obtain the Prime Key to unlock the Vault of Secrets.
"""
def check_prime(m):
    flag=0
    if m<1: #0 or -1
        flag=1
    elif m==1: #prime no is number is divisible by itself and 1
         flag==0
    else:
        #2 to n check
        for i in range(2,(m//2)+1):
           if m%i==0:
             flag=1
             break
    
    if flag==0:   
      return 1
    else:
      return 0
result=[] #at last list is converted to tuple
N=int(input("enter number:"))

flag=0
k=N+1
while flag<1:
   flag=check_prime(k)
   if flag==1:
       result.append(k)
   else:
        #check next element #flag is 1 to stop
       k=k+1
       #2
sum=0
for i in range(N+1,k):
    sum+=i
result.append(sum)

p1=k#k is smallest prime no
flag=0
k=p1+1
while flag<1:# check prime or not .here call function ie check_prime to check k is prime or not.
   flag=check_prime(k)
   if flag==1:
       p2=k
   else:
        #check next element 
        #flag is 1 to stop
       k=k+1
p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)
prime_key=tuple(result)
print(prime_key)
#Output :
"""
    7
    (11, 27, False)
"""