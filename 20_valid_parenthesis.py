"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Example 5:

Input: s = "([)]"
Output: false
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {")": "(", "]": "[", "}": "{"}

        for br in s:
            if br in closeOpen:
                if not stack or stack[-1] != closeOpen[br]:
                    return False
                stack.pop()
            else:
                stack.append(br)

        return len(stack) == 0
