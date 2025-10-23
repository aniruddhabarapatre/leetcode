"""
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q.
If either node p or q does not exist in the tree, return null.
All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants
(where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.


Example 3:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h)
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Helper function to perform DFS and find LCA
        def dfs(node):
            if not node:
                return None, False, False

            left_lca, left_p_found, left_q_found = dfs(node.left)
            right_lca, right_p_found, right_q_found = dfs(node.right)

            p_found = left_p_found or right_p_found or node == p
            q_found = left_q_found or right_q_found or node == q

            # If LCA already found in left subtree
            if left_lca:
                return left_lca, p_found, q_found
            # If LCA already found in right subtree
            if right_lca:
                return right_lca, p_found, q_found

            # If current node is LCA
            if p_found and q_found:
                return node, p_found, q_found

            return None, p_found, q_found

        lca, p_exists, q_exists = dfs(root)
        return lca if p_exists and q_exists else None
