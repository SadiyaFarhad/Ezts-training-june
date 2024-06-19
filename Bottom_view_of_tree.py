#Printing bottom view elements of a tree

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

class node_data:
    def __init__(self,node,HKey):
        self.node=node
        self.HKey=HKey
        
def bottomview(root):
    temp=node_data(root,0)
    Q=[temp]
    Q.append(None)
    key_Dict={}
    
    while len(Q)!=0:
        curr=Q.pop(0)
        if curr==None: 
            if len(Q)==0: 
                break
            else:
               Q.append(None)
        else: 
            
            key_Dict[curr.HKey]=curr.node.value
        
            if curr.node.left!=None:
                temp=node_data(curr.node.left,curr.HKey-1)
                Q.append(temp)
        
            if curr.node.right!=None:
                temp=node_data(curr.node.right,curr.HKey+1)
                Q.append(temp)
                
    for i in sorted(key_Dict):
        print(key_Dict[i],end=' ')
    print(key_Dict)
    
if __name__=="__main__":
     root=node(1)
     root.left=node(2)
     root.right=node(3)
     root.left.left=node(4)
     root.left.right=node(5)
     root.right.left=node(6)
     root.right.right=node(7)
     root.left.right.left=node(9)
     root.left.right.right=node(10)
     root.right.right.right=node(11)
     root.left.right.left.left=node(12)
     root.left.right.left.right=node(13)
     print("bottom view elements")
     #print(root)
     bottomview(root)
"""
OUTPUT:
bottom view elements
12 9 13 10 7 11 {0: 13, -1: 9, 1: 10, -2: 12, 2: 7, 3: 11}
"""