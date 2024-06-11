
"""
Program to calculate the Power of two numbers using recursion
Created on Tue Jun 11 10:43:58 2024

@author: Sadiya Farhad
"""

def power(base,exponent):
     if exponent==0:
         return 1
     else:
         return base * power(base,exponent-1)
result=power(3,3)
print(result)
#Output: 8