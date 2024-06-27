# BELLMAN FORD ALGORITHM  TO COMPUTES SHORTEST PATHS FROM SINGLE SOURCE TO ALL OF OTHER VERTICES IN WEIGHTED DIRECTED GRAPH
g=[
   [0,6,4,5,False,False],
   [False,0,False,False,-1,False],
   [False,-2,0,False,3,False],
   [False,False,-2,0,False,-1],
   [False,False,False,False,0,3],
   [False,False,False,False,False,0]
]  

E_L= []
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j]!=False and g[i][j]!=0:
            E_L.append(tuple((i,j)))
print(E_L)
dist={}
for i in range(len(g)):
    dist[i]=float("inf")
dist[0]=0
print(dist)
for i in range(len(g) - 1):
    for j in E_L:
        new_dist=dist[j[0]]+g[j[0]][j[1]]
        if dist[j[1]]>new_dist:
            dist[j[1]]=new_dist
print(dist)