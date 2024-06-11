
"""
Sum of Digits of a number using Recursion
Created on Tue Jun 11 20:56:33 2024

"""
def sumofdigits(n):
    if n==0:
        return 0
    return n%10+sumofdigits(n//10)
n=7634
print(sumofdigits(n)) # Output will be 20
