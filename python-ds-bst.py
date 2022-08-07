from queue import Queue


class BSTNode:
    def __init__(self, value) -> None:
        self.data = value
        self.left = None
        self.right = None
            
def inorder_traversal(root):
    if root:   
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:   
        print(root.data)
        inorder_traversal(root.left)
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:   
        inorder_traversal(root.left)
        inorder_traversal(root.right)
        print(root.data)


def preorder_traversal_iter(root):
    if root:   
        print(root.data)
        inorder_traversal(root.left)
        inorder_traversal(root.right)

def find_max_iterative(root):
    if not root:
        return

    q = Queue.queue()
    node = root
    q.enqueue(node)
    max = float("-inf")

    while not q:
        q.get






# Driver code
root = BSTNode(1)
root.left = BSTNode(2)
root.right = BSTNode(3)
root.left.left = BSTNode(4)
root.left.right = BSTNode(5)
print("Inorder traversal of binary tree is")
result = []
inorder_traversal(root)
print("\n")
preorder_traversal(root)
print("\n")
postorder_traversal(root)
print("\n")
preorder_traversal_iter(root)


#print(result)
