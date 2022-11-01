
## Get max dept of a BT

from fcntl import F_SEAL_SEAL


def get_max_depth(self, root):
    if not root:
        return 0

    return 1 + max(self.get_max_depth(root.left), self.get_max_depth(root.right))


## Same BT

def same_tree(p, q):

    def recur(first, second):
        if first is None and second is None:
            return True
        
        elif (first is None and second is not None) or (first is not None and second is None):
            return False

        if first.val != second.val:
            return False
        
        return recur(first.left, second.left) and recur(first.right, second.right)
    
    return recur(p, q)


## invert a BT

def invert_bt(root):
    if not root:
        return
    
    root.left, root.right = root.right, root.left

    invert_BT(root.left)
    invert_BT(root.right)
    return root

# Btree maximum path sum.




# BT level order traversal

def level_order_traverse(root):

    q = []
    q.append(root) 
    while q:
        node = q.pop(0)
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
            
    


        

        
    
