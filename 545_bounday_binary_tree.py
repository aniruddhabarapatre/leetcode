"""
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node is in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Example 1:

Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(h) where h is the height of the tree
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # leaf validator
        def is_leaf(node):
            return node and not node.left and not node.right

        # add left boundary excluding leaves
        def add_left_boundary(node):
            while node:
                if not is_leaf(node):
                    boundary.append(node.val)
                node = node.left if node.left else node.right

        # add leaves
        def add_leaves(node):
            if is_leaf(node):
                boundary.append(node.val)
                return
            if node.left:
                add_leaves(node.left)
            if node.right:
                add_leaves(node.right)

        # add right boundary excluding leaves
        def add_right_boundary(node):
            stack = []
            while node:
                if not is_leaf(node):
                    stack.append(node.val)
                node = node.right if node.right else node.left
            while stack:
                boundary.append(stack.pop())  # reverse order

        boundary = [root.val] if not is_leaf(root) else []

        add_left_boundary(root.left)
        add_leaves(root)
        add_right_boundary(root.right)

        return boundary
