from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_traversal(root):
    if not root:
        return []
    
    result = []
    current_level = deque([root])
    left_to_right = True
    
    while current_level:
        level_size = len(current_level)
        level_nodes = deque()
        
        for _ in range(level_size):
            node = current_level.popleft()
            if left_to_right:
                level_nodes.append(node.value)
            else:
                level_nodes.appendleft(node.value)
            
            if node.left:
                current_level.append(node.left)
            if node.right:
                current_level.append(node.right)
        
        result.append(list(level_nodes))
        left_to_right = not left_to_right
    
    return result

# Example usage:
# Constructing a binary tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(zigzag_traversal(root))  # Output: [[1], [3, 2], [4, 5, 6, 7]]
