# -*- coding: utf-8 -*-
"""
Space Counter:
* You have been given the task of making the content on a social media platform more user-friendly.
* Your task is to find and return an integer value representing count of the number of spaces in a given string s.
"""

s=input("enter string : ")
c=0
for i in range(0,len(s)):
    if s[i]==" ":
        c+=1
print("Number of spaces:",c)
"""
Output
enter string : sadiya is in best120 batch
Number of spaces: 4
"""
