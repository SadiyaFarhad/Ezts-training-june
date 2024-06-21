#AVL TREE:
class node:#class for tree node
    def __init__(self,data): #define linked list for node
        self.val=data
        self.left=None
        self.right=None
        self.height=1#first node height is one always
def insert(root,super): 
    if not root:
            return node(super)
    if super<root.val:
            root.left=insert(root.left,super)
    else:
            root.right=insert(root.right,super)
    root.height=1+max(ght(root.left),ght(root.right))
    bf=getbf(root)
        #RR rotation
    if bf>1 and super<root.left.val:
            return rightRotate(root)
        #RL rotation
    if bf>1 and super>root.left.val:
            root.left=leftRotate(root.left) 
            return rightRotate(root)
        #LL rotation
    if bf<-1 and super>root.right.val:
            return leftRotate(root)
        #LR rotation
    if bf<-1 and super<root.right.val:
            root.right=rightRotate(root.right)
            return leftRotate(root)
    return root
            
def ght(root): 
    if not root: 
        return 0
    return root.height
def getbf(root):
        if not root:
            return 0
        return ght(root.left)-ght(root.right)
def leftRotate(A):
        B=A.right
        temp=B.left
        B.left=A
        A.right=temp
        #height of both a and b updaed
        A.height=1+max(ght(A.left),ght(A.right))
        B.height=1+max(ght(B.left),ght(B.right))
        return B
def rightRotate(A):
         B=A.left
         temp=B.right
         B.right=A
         A.left=temp
         #height of both a and b updaed
         A.height=1+max(ght(A.left),ght(A.right))
         B.height=1+max(ght(B.left),ght(B.right))
         return B
         
        
def inorder(root): #print the data inorder format
        if not root:
            return
        inorder(root.left)
        print(root.val)
        inorder(root.right)
if __name__=="__main__":
    root=None
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i)
    inorder(root)
    
    
        
