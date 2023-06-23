# time: O( h ), where 'h' is the height of the tree
class BSTNode:
    def __init__(self, parent, key, data=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.data = data

def search(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None

def min_key(root):
    while root.left is not None:
        root = root.left
    return root

def max_key(root):
    while root.right is not None:
        root = root.right
    return root

def insert(root, key, data):
    parent = root.parent
    while root is not None:
        if root.key == key:
            root.data = data
            return
        elif key < root.key:
            parent = root
            root = root.left
        else:
            parent = root
            root = root.right
    if parent.key > key:
        parent.left = BSTNode(parent, key, data)
    else:
        parent.right = BSTNode(parent, key, data)
    return True

def succesor(root, key):
    root = search(root, key)
    if root is None:
        return None

    if root.right is not None:
        return min_key(root.right)
    else:
        parent = root.parent
        while parent is not None:
            if root == parent.left:
                return parent
            root = parent
            parent = parent.parent
        return None

def predecessor(root, key):
    root = search(root, key)
    if root is None:
        return None

    if root.left is not None:
        return max_key(root.left)
    else:
        parent = root.parent
        while parent is not None:
            if root == parent.right:
                return parent
            root = parent
            parent = parent.parent
        return None

def remove(root, key):
    root = search(root, key)
    if root is None:
        return None

    # no kids
    if root.right is None and root.left is None:
        if root.parent.left == root:
            root.parent.left = None
        else:
            root.parent.right = None
        root.parent = None

    # left kid
    elif root.right is None:
        root.left.parent = root.parent
        if root.parent.left == root:
            root.parent.left = root.left
        else:
            root.parent.right = root.left
        root.parent = None
        root.left = None

    # right kid
    elif root.left is None:
        root.right.parent = root.parent
        if root.parent.left == root:
            root.parent.left = root.right
        else:
            root.parent.right = root.right
        root.parent = None
        root.right = None

    # both kids
    else:
        succ = succesor(root, key)
        # connecting succesor sub-tree
        if succ.right is not None:
            succ.right.parent = succ.parent
            succ.parent.left = succ.right

        # changing succ into root
        succ.right = root.right
        succ.left = root.left
        root.left.parent = succ
        root.right.parent = succ
        succ.parent = root.parent
        if root.parent.left == root:
            root.parent.left = succ
        else:
            root.parent.right = succ
        root.parent = None
        root.right = None
        root.left = None
    return True
