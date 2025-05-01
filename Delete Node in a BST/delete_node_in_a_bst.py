"""
This module provides functionality to delete a node from a binary search tree.
"""

from collections import deque

class TreeNode:
    """
    A class representing a node in a binary tree.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_by_levels(node):
    """
    Sort a binary tree by levels.
    """
    if node is None:
        return []
    result = [node.val]
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if not current.left and current.right:
            result.append(None)
        if current.left:
            queue.append(current.left)
            result.append(current.left.val)
        if not current.right and current.left:
            result.append(None)
        if current.right:
            queue.append(current.right)
            result.append(current.right.val)
    return result


class Solution:
    """
    This class provides a method to delete a node from a binary search tree (BST).
    """
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        Deletes a node with the given key from the BST.
        """
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = root.right
            while node.left:
                node = node.left
            node.left = root.left
            return root.right
        return root


if __name__ == '__main__':
    a = TreeNode(2)
    b = TreeNode(4)
    c = TreeNode(3, a, b)
    d = TreeNode(7)
    e = TreeNode(6, left=None, right=d)
    f = TreeNode(5, c, e)

    solution = Solution()
    print(tree_by_levels(f))
    print(solution.deleteNode(f, 3))
    print(tree_by_levels(f))
    # Output: [5, 2, 6, None, 4, None, 7] or [5, 4, 6, 2, None, None, 7]
