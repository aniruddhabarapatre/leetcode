"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List


class Solution:
    # Time complexity: O(4^n / sqrt(n)) (Catalan number)
    # Space complexity: O(4^n / sqrt(n))
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open if open < n
        # add closing if closed < open
        # valid iff open == closed == n
        result = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return result
