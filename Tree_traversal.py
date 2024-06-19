#TREE TRAVERSAL - INORDER ,POSTORDER & PREORDER TRAVERSAL
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
pre=[]
post=[]
In=[]
def preorder(root):
    if root==None:
        return 
    else:
        pre.append(root.value)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root==None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        post.append(root.value)
def inorder(root):
    if root==None:
        return
    else:
        inorder(root.left)
        In.append(root.value)
        inorder(root.right)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    preorder(root)
    postorder(root)
    inorder(root)
print("the preorder traversal of tree:")
print(pre)
print("the postorder traversal of tree:")
print(post)
print("the inorder traversal of tree:")
print(In)
"""
OUTPUT
the preorder traversal of tree:
[1, 2, 4, 5, 3, 6, 7]
the postorder traversal of tree:
[4, 5, 2, 6, 7, 3, 1]
the inorder traversal of tree:
[4, 2, 5, 1, 6, 3, 7]
"""