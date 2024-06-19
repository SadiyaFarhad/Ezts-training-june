
#Printing Left view and Right view of tree
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def Left_View(root):
    Q=[root]
    Q.append(None)
    print(root.value,end=' ')
    while len(Q)>0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                print(Q[0].value,end=' ')
                Q.append(None)
        else:
            if cur.left!=None:
                Q.append(cur.left)
            if cur.right!=None:
                Q.append(cur.right)
def Right_View(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                Q.append(None)
        else:
            if Q[0]==None:
                print(cur.value,end=' ')
            if cur.left!=None:
                Q.append(cur.left)
            if cur.right!=None:
                Q.append(cur.right)
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
    print('Left View elements')
    Left_View(root)
    print('\nRight View elements')
    Right_View(root)

"""
OUTPUT:
Left View elements
1 2 4 9 12 
Right View elements
1 3 7 11 13
"""