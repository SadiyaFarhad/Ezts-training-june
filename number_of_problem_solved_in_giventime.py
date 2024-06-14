"""
Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 PM and will run until midnight (12 AM) i.e., for 4 hours. 
The contest comprises of N problems that are arranged in order of difficulty, with problem 1 being the simplest and problem N being the most difficult. 
Max is aware that he will require 5*i minutes to solve the ith problem.
You will be give the Start time as T. 
Your task is to find and return an integer value, representing the number of problems Max can solve and 
reach the party venue within the given time frame of 4 hours.
""" 
while True:
   n=int(input("enter the time(1-8) he started: "))
   if n>1 and n<=8:
     s=(8-n)*60
     break
   else:
     print("invalid number")
    
print(f"time available={s}min")
count=0
i=5
while s>0:
    s=s-i
    i=i+5
    count=count+1
    if i>s:
        break
print(f"number of problems solved = {count}")
"""
OUTPUT: enter the time(1-8) he started: 6
time available=120min
number of problems solved = 6

"""