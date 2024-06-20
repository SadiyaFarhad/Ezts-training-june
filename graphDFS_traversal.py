#DFS graph traversal.

a={1:[(1,2,0),(1,3,0)],
   2:[(2,1,0),(2,7,0)],
   3:[(3,1,0),(3,6,0),(3,5,0)],
   4:[(4,7,0),(4,8,0)],
   5:[(5,3,0),(5,7,0)],
   6:[(6,3,0),(6,8,0)],
   7:[(7,2,0),(7,5,0),(7,4,0)],
   8:[(8,4,0),(8,6,0)]}
v={
   1:False,
   2:False,
   3:False,
   4:False,
   5:False,
   6:False,
   7:False,
   8:False}
s=[] #stack
def dfs(a,v,s,e):
    if v[e]==False: # if element is not visited
        s.append(e) # add element to the stack
        v[e]=True   # mark element as visited
    else:
        return  
    for i in a[e]: #loop iterates for each tuples in list a[e]
        dfs(a,v,s,i[1]) #dfs function called recursively with i[1] as new node to visit.
    print(s.pop()) #pop element and print it
   
dfs(a,v,s,1) #calling DFS method 
"""
OUTPUT:
4
8
6
3
5
7
2
1
"""