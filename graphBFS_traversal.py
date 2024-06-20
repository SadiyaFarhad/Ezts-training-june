#BFS graph traversal,

    
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

def bfs(a,e):
    q=[e] #first element add to the Queue
    v={}
    for i in a.keys():
        v[i]=False                  #All other elemnet are not visited
    v[e]=True                       #First element is visited
    while len(q)!=0:                #Queue is not mpty
        curr=q.pop(0)               #Pop the first element
        print(curr)                 #Print the first element
        for i in a[curr]:
                if v[i[1]]==False:  #If not visited then visit it
                    q.append(i[1])
                    v[i[1]]=True    #Mark it visited 
           
bfs(a,1)                            #call the BFS function
"""
OUTPUT:
1
2
3
7
6
5
4
8
"""