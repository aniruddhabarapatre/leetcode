"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]


Example 2:

Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]


Example 3:

Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
"""

# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])  # node, col
        min_col, max_col = 0, 0
        cols = defaultdict(list)  # cols index -> list of values

        while q:
            node, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            cols[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))

            if node.right:
                q.append((node.right, col + 1))

        return [cols[c] for c in range(min_col, max_col + 1)]
