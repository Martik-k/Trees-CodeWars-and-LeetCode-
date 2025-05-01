"""
This function sorts a binary tree by levels.
"""

from collections import deque

class Node:
    """
    A class representing a node in a binary tree.
    """
    def __init__(self, L, R, n):
        """
        Initialize a node with left child, right child, and value.
        """
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    """
    Sort a binary tree by levels.
    """
    if node is None:
        return []
    result = []
    queue = deque([node])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

if __name__ == '__main__':
    a = Node(None, None, 1)
    b = Node(None, None, 3)
    c = Node(a, b, 8)
    d = Node(None, None, 4)
    e = Node( None, None, 5)
    f = Node(d, e, 9)
    g = Node(c, f, 2)

    print(tree_by_levels(g))