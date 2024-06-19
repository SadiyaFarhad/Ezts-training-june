#Print Height of a Tree 
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
    
def height(root):
    if root==None:
        return 0
    
    lh=height(root.left)
    rh=height(root.right)
    h=max(lh,rh)+1
    return h #none
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
    h=height(root)#print(height(root))
    print("the height of tree is: ",h)
    
#output : the height of tree is 5