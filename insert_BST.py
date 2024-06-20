#create Binary Search Tree (BST) from the list E and then performing an in-order traversal to print the values in sorted order.
class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    @staticmethod
    def ins_bst(root, val):
        if root == None:
            return Node(val)
        if val < root.value:
            root.left = Node.ins_bst(root.left, val)
        if val > root.value:
            root.right = Node.ins_bst(root.right, val)
        return root

    @staticmethod
    def inorder(root):
        if root:
            Node.inorder(root.left)
            print(root.value)
            Node.inorder(root.right)

# List of values to be inserted into the BST
E = [4, 6, 7, 3, 8, 2, 5, 9, 1]
# Initialize the root with the first element
root = Node(E.pop(0))
# Insert the rest of the values into the BST
for i in E:
    root = Node.ins_bst(root, i)
# Perform an in-order traversal and print the values
Node.inorder(root)
"""
OUTPUT:
1
2
3
4
5
6
7
8
9
"""
