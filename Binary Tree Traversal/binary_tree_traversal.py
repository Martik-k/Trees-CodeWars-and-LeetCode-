class Node:
    """
    A class representing a node in a binary tree.
    """
    def __init__(self, data):
        """
        Initialize a node with data and no children.
        """
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """
        Return a string representation of the node.
        """
        return f"Node({self.data})"

# Pre-order traversal
def pre_order(node):
    """
    Pre-order traversal of a binary tree.
    """
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    """
    In-order traversal of a binary tree.
    """
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    """
    Post-order traversal of a binary tree.
    """
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]


if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    print(pre_order(a))
    print(in_order(a))
    print(post_order(a))
