
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

         
# DFS

# PREORDER TRAVERSAL  --> (ROOT, LEFT, RIGHT)

def preorder_traversal(node):
    if node is None:
        return
    
    print(node.val)
    preorder_traversal(node.left)
    preorder_traversal(node.right)
