chocolate jar
You are given an integer array of size N, representing jars of chocolates. Three students A, B, and C respectively, will pick chocolates one by one from each chocolate jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task is to fine and return an integer value representing the total number of chocolates that student A will have, after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.
Input Format:
Input1: An integer array representing the quantity of chocolates in each jar. Input2: An integer value N representing the number of jars
Output Format: Return an integer value representing the total number of chocolates that student A will have, after all the chocolates are picked.

Solution:

jars=list(map(int,input().split())) n=int(input())
a=0
for i in jars:
print("this iteration is for",i) a=a+(i//3)
print(a) #remainder if i%3!=0:
a=a+1 else:
a=a+0 print(a)
Output
10 20 30
3
this iteration is for 10 3
this iteration is for 20 10
this iteration is for 30 21
21
