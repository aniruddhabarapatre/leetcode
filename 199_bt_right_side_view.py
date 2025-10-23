"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.


Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]


Example 2:

Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]


Example 3:

Input: root = [1,null,3]
Output: [1,3]


Example 4:

Input: root = []
Output: []
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(w)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result

    # Variant: left and right side view
    def left_side_view(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        left_view, right_view = [], []

        while q:
            level_size = len(q)
            first_node, last_node = None, None

            for i in range(level_size):
                node = q.popleft()
                if i == 0:
                    first_node = node

                if i == level_size - 1:
                    last_node = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            left_view.append(first_node.val)
            right_view.append(last_node.val)

        # left_view bottom → top, right_view top → bottom
        left_view.reverse()

        # merge and avoid duplicate root
        combined = left_view + right_view[1:]
        return combined
